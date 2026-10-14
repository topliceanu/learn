package reader

import (
	"bufio"
	"bytes"
	"context"
	"fmt"
	"net/http"

	"github.com/topliceanu/log/pkg/types"
)

// httpReadCloser reads logs from a URL
type httpReadCloser struct {
	resp    *http.Response
	scanner *bufio.Scanner
}

func NewHTTPReadCloser(ctx context.Context, cfg types.HTTPReaderConfig) (types.ReadCloser, error) {
	resp, err := http.Get(cfg.URL.String())
	if err != nil {
		return nil, fmt.Errorf("failed to fetch HTTP resource: %w", err)
	}
	scanner := bufio.NewScanner(resp.Body)
	scanner.Buffer(make([]byte, cfg.MaxLineSizeBytes), int(cfg.MaxLineSizeBytes))
	return &httpReadCloser{resp, scanner}, nil
}

func (h *httpReadCloser) Read(ctx context.Context) ([]byte, error) {
	if h.scanner.Scan() {
		return bytes.Clone(h.scanner.Bytes()), nil
	}
	return nil, h.scanner.Err()
}

func (h *httpReadCloser) Close() error {
	return h.resp.Body.Close()
}

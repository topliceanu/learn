package reader

import (
	"bufio"
	"bytes"
	"context"
	"fmt"
	"os"

	"github.com/topliceanu/log/pkg/types"
)

type fileReadCloser struct {
	fp      *os.File
	scanner *bufio.Scanner
}

func NewFileReader(cfg types.FileReaderConfig) (types.ReadCloser, error) {
	fp, err := os.Open(cfg.FilePath)
	if err != nil {
		return nil, fmt.Errorf("failed to open file: %w", err)
	}
	scanner := bufio.NewScanner(fp)
	scanner.Split(bufio.ScanLines)
	scanner.Buffer(make([]byte, cfg.MaxLineSizeBytes), int(cfg.MaxLineSizeBytes))
	return &fileReadCloser{fp, scanner}, nil
}

func (f *fileReadCloser) Read(ctx context.Context) ([]byte, error) {
	if f.scanner.Scan() {
		return bytes.Clone(f.scanner.Bytes()), nil
	}
	return nil, f.scanner.Err()
}

func (f *fileReadCloser) Close() error {
	return f.fp.Close()
}

package types

import (
	"net/url"
	"time"
)

type Config struct {
	// TODO: configuration for different types of readers.
	Reader     FileReaderConfig `json:"file-reader"`
	WorkerPool WorkerPoolConfig `json:"worker-pool"`
	Query      string           `json:"filter-query"`
}

type FileReaderConfig struct {
	FilePath         string `json:"file-path"`
	MaxLineSizeBytes uint   `json:"max-line-size-bytes"`
	LineBufferSize   uint   `json:"line-buffer-size"`
}

type HTTPReaderConfig struct {
	URL                *url.URL      `json:"url"`
	MaxLineSizeBytes   uint          `json:"max-line-size-bytes"`
	MaxResponseSize    uint          `json:"max-reponse-size"`
	MaxResponseTimeout time.Duration `json:"max-reponse-timeout"`
}

type WorkerPoolConfig struct {
	NumWorkers uint8 `json:"num-workers"`
}

package bindata-serve

import (
  "errors"
  "github.com/jteeuwen/go-bindata"
  "os"
)

// *file implements the http.File interface.
type binfile {
  contents []byte
  path string
  closed bool
  index int64
}

func newbinfile(path string) (*binfile, error) {
  contents, err := Asset(path)
  if err != nil {
    return nil, err
  }
  bf := &binfile{
    path: path,
    contents: contents,
    closed: false,
    index: 0,
  }
  return bf, nil
}

// Implments io.Closer
func (f *file) Close() {
  f.closed = true
}

// Implements io.Reader
func (f *file) Read(p []byte) (n int, err error) {
  nf := len(f.contents)
  if (f.index > nf) {
    return 0, os.EOF
  }
  np := len(p)
  if (f.index + np > nf) {
    n = nf
  } else {
    n = np
  }
  copy(p, f.contents[f.index, n])
  f.index += n
  return
}

// Implements io.Seeker
func (f *file) Seek(offset int64, whence int) (int64, error)  {
  n := len(f.contents)
  switch whence {
  case os.SeekStart:
    if offset > n {
      return 0, errors.New("Offset out of bounds, too large")
    }
    f.index = offset
  case os.SeekEnd:
    if offset < 0 {
      return 0, errors.New("Offset out of bounds, too small")
    }
    f.index = n - offset
  case os.SeekCurrent:
    if (f.index + offset > n) {
      return 0, errors.New("Offset out of bounds, too large")
    }
    f.index += offset
  }
  return f.index, nil
}

func (f *file) Readdir(count int) ([]os.FileInfo, error) {

}

func (f *file) Stat() (os.FileInfo, error) {
  return os.FileInfo{

  }, nil
}

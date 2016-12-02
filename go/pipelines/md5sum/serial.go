package main

import (
	"crypto/md5"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"sort"
)

func md5All(root string) (hashes map[string][md5.Size]byte, err error) {
	hashes = make(map[string][md5.Size]byte)
	err = filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		var (
			data []byte
		)
		if err != nil {
			return err
		}
		if info.Mode().IsRegular() == false {
			return nil
		}
		data, err = ioutil.ReadFile(path)
		if err != nil {
			return err
		}
		hashes[path] = md5.Sum(data)
		return nil
	})
	return hashes, err
}

func main() {
	var (
		err   error
		i     int
		m     map[string][md5.Size]byte
		p     string
		paths []string
	)
	m, err = md5All(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}
	paths = make([]string, len(m))
	i = 0
	for p = range m {
		paths[i] = p
		i += 1
	}
	sort.Strings(paths)
	for _, p = range paths {
		fmt.Printf("%x %s\n", m[p], p)
	}
}

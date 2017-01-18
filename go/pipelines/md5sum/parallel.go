package main

import (
	"crypto/md5"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"sort"
)











func walker(done <-chan struct{}, root string) <-chan string {
	var paths = make(chan string)
	go func() {
		defer close(paths)
		var (
			err error
		)
		err = filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if info.Mode().IsRegular() == false {
				return nil
			}
			select {
			case paths <- path:
			case <-done:
				return // this always selects if done channel is closed
			return nil
		})
		if err != nil {
			fmt.Println(err)
		}
	}()
	return paths
}

func md5sum(paths <-chan string) <-chan *sum {
	out := make(chan *sum)
	go func() {
		defer close(out)
		for p := range paths {
			data, err := ioutil.ReadFile(p)
			if err != nil {
				fmt.Println(err)
				continue
			}
			out <- &sum{p, md5.Sum(data)}
		}
	}()
	return out
}

type sum struct {
	path string
	hash [md5.Size]byte
}

func md5All(root string) (hashes map[string][md5.Size]byte, err error) {
	hashes = make(map[string][md5.Size]byte)
	paths := walker(root)
	sums := md5sum(paths)
	for s := range sums {
		hashes[s.path] = s.hash
	}
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

package main

import (
	"context"
	"crypto/md5"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

type Job struct {
	path string
	err  error
	data []byte
	sum  [md5.Size]byte // MD5 sum
}

// walk takes a single root folder path, treverses it completely and return a channel of jobs to be performed
func walk(ctx context.Context, root string) <-chan *Job {
	var out = make(chan *Job)
	go func() {
		defer close(out)
		filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			if info.Mode().IsRegular() == false {
				return nil
			}
			select {
			case <-ctx.Done():
				return nil
			case out <- &Job{path}:
			}
		})
	}()
	return out
}

func read(ctx context.Context, jobs <-chan *Job) <-chan *Job {
	var out = make(chan *Job)
	go func() {
		defer close(out)
		var j *Job
		var data []byte
		var err error
		for j = range jobs {
			if j.err != nil {
				continue
			}
			data, err = ioutil.ReadFile(path)
			j.err = err
			j.data = data
			select {
			case <-ctx.Done():
				return
			case out <- j:
			}
		}
	}()
	return out
}

func md5sum(ctx context.Context, jobs <-chan *Job) <-chan *Job {
	var out = make(chan *Job)
	go func() {
		defer close(out)
		var j *Job
		for j = range jobs {
			j.sum = md5.Sum(j.data)
			select {
			case <-ctx.Done():
				return
			case out <- j:
			}
		}
	}()
	return out
}

func main() {
	var (
		ctx, cancel = context.WithCancel(context.Background())
		c1, c2, c3  chan *Job
		j           Job
	)
	c1 = walk(ctx, os.Args[1])
	c2 = read(ctx, c1)
	c3 = md5sum(ctx, c2)
	for j = range c3 {
		if j.err != nil {
			fmt.Println("error: %+v\n", j.err)
		} else {
			fmt.Printf("%x %s", j.sum, j.text)
		}
	}
}

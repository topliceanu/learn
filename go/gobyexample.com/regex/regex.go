package main

import (
	"fmt"
	"regexp"
)

func main() {
	r := "p([a-z]+)ch"
	match, _ := regexp.MatchString(r, "peach")
	fmt.Println("Matched", match)

	re, err := regexp.Compile(r)
	if err != nil {
		panic(err)
	}

	fmt.Println(re.MatchString("peach"))
	fmt.Println(re.FindString("peaches are the greatest"))
	fmt.Println(re.FindStringIndex("where is the peach?"))
	fmt.Println(re.FindStringSubmatch("peach punch"))
	fmt.Println(re.FindStringSubmatchIndex("peach punch"))
	fmt.Println(re.FindAllString("peach punch pinch", -1))
	fmt.Println(re.ReplaceAllString("a peach", "<fruit>"))
}

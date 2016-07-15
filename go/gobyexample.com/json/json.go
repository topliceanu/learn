package main

import (
	"encoding/json"
	"fmt"
)

type Response struct {
	Page int `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {
	bval, _ := json.Marshal(true)
	fmt.Printf("%s(%T)\n", string(bval), bval)

	aval, _ := json.Marshal([]string{"apple", "orange", "pear"})
	fmt.Printf("%s(%T)\n", string(aval), aval)

	sval, _ := json.Marshal(Response{1, []string{"apple", "pear"}})
	fmt.Printf("%s(%T)\n", string(sval), sval)

	var r Response
	s := []byte(`{"page": 1, "fruits": ["apple", "pear", "orange"]}`)
	err := json.Unmarshal(s, &r)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%+v(%T)\n", r, r)
}

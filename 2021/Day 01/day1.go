package main

import (
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	data, error := os.ReadFile("day1.txt")
	check(error)
	fmt.Print(string(data))
}

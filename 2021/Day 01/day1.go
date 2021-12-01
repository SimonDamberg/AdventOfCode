package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("day1.txt")
	defer file.Close()

	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	var lines []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		val, err1 := strconv.Atoi(scanner.Text())
		if err1 != nil {
			log.Fatalf("readLines: %s", err)
		}
		lines = append(lines, val)
	}

	var noIncreases int = 0
	var noIncreases2 int = 0
	for i, v := range lines {
		if i > 0 {
			if v > lines[i-1] {
				noIncreases++
			}
		}
		if i >= 3 {
			if v+lines[i-1]+lines[i-2] > lines[i-1]+lines[i-2]+lines[i-3] {
				noIncreases2++
			}
		}
	}
	fmt.Printf("Part1: %d\n", noIncreases)
	fmt.Printf("Part2: %d", noIncreases2)
}

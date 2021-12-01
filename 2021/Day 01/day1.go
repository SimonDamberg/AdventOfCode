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

	var prev1 int = 0
	var prev2 int = 0
	var prev3 int = 0

	var noIncreases int = 0
	var noIncreases2 int = 0
	for i, v := range lines {
		if i > 0 {
			if v > lines[i-1] {
				noIncreases++
			}
		}
		if i >= 3 {
			if v+prev2+prev3 > prev1+prev2+prev3 {
				noIncreases2++
			}
		}
		prev1 = prev2
		prev2 = prev3
		prev3 = v
	}
	fmt.Printf("Part1: %d\n", noIncreases)
	fmt.Printf("Part2: %d", noIncreases2)
}

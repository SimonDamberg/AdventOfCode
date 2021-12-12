package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
)

func ReadFileToStr(fileName string) []string {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		val := scanner.Text()
		lines = append(lines, val)
	}
	return lines
}

func day10(lines []string) {
	points := map[string]int{
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137,
	}

	validOpenBrackets := []string{"(", "[", "{", "<"}
	validBracketPairs := map[string]string{
		")": "(",
		"]": "[",
		"}": "{",
		">": "<",
	}

	var part1 int
	var part2 []int
	for _, line := range lines {
		var openBrackets []string
		var corruptedBracket string
		foundCorrupt := false
		for _, c := range line {
			foundOpenBracket := false
			for _, v := range validOpenBrackets {
				if string(c) == v {
					openBrackets = append(openBrackets, v)
					foundOpenBracket = true
					break
				}
			}
			if !foundOpenBracket {
				// Pop last opening bracket
				lastOpenBracket := openBrackets[len(openBrackets)-1]
				openBrackets = openBrackets[:len(openBrackets)-1]
				if validBracketPairs[string(c)] != lastOpenBracket {
					foundCorrupt = true
					corruptedBracket = string(c)
					break
				}
			}
		}
		if foundCorrupt {
			// Part 1
			part1 += points[corruptedBracket]
		} else {
			// Part 2
			score := 0
			for len(openBrackets) > 0 { // Only brackets left are the ones that were not closed
				lastOpenBracket := openBrackets[len(openBrackets)-1]
				openBrackets = openBrackets[:len(openBrackets)-1]
				switch lastOpenBracket {
				case "(":
					score = score*5 + 1
				case "[":
					score = score*5 + 2
				case "{":
					score = score*5 + 3
				case "<":
					score = score*5 + 4
				}
			}
			part2 = append(part2, score)
		}
	}
	sort.Ints(part2)
	fmt.Printf("Part1: %d\n", part1)
	fmt.Printf("Part2: %d\n", part2[len(part2)/2])
}

func main() {
	lines := ReadFileToStr("day10.txt")
	day10(lines)
}

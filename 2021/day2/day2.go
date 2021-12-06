package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func ReadFileToStr(fileName string) []string {
	file, err := os.Open(fileName)
	defer file.Close()

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

func main() {
	lines := ReadFileToStr("day2.txt")
	var horizontal, depth, depth2, aim int
	for _, v := range lines {
		s := strings.Split(v, " ")
		amt, _ := strconv.Atoi(s[1])
		switch s[0] {
		case "forward":
			horizontal += amt   // Part 1 & 2
			depth2 += amt * aim // Part 2
		case "up":
			depth -= amt // Part 1
			aim -= amt   // Part 2
		case "down":
			depth += amt // Part 1
			aim += amt   // Part 2
		}
	}
	fmt.Printf("Part1: %d\n", depth*horizontal)
	fmt.Printf("Part2: %d\n", depth2*horizontal)
}

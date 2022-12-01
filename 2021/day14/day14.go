package main

import (
	"bufio"
	"log"
	"os"
	"strings"
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

func main() {
	lines := ReadFileToStr("day14.txt")
	startWord := lines[0]
	sequences := make(map[string]string)

	for _, line := range lines[2:] {
		s := strings.Split(line, " -> ")
		sequences[s[0]] = s[1]
	}
	log.Printf("Start word: %s", startWord)
	log.Printf("Sequences: %v", sequences)
}

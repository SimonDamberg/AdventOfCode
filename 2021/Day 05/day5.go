package main

import (
	"bufio"
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

func removeWhitespace(input []string) []string {
	var output []string
	for _, val := range input {
		output = append(output, strings.TrimSpace(val))
	}
	return output
}

func parseInput(lines []string) [][]int {
	var result [][]int // always 4 values per array
	for _, line := range lines {
		split := strings.Split(line, "->")
		first := removeWhitespace(strings.Split(split[0], ","))
		second := removeWhitespace(strings.Split(split[1], ","))

		var row = make([]int, 4)
		row[0], _ = strconv.Atoi(first[0])
		row[1], _ = strconv.Atoi(first[1])
		row[2], _ = strconv.Atoi(second[0])
		row[3], _ = strconv.Atoi(second[1])
		result = append(result, row)
	}
	return result
}

func countCross(input [1000][1000]int) int {
	var result int
	for _, row := range input {
		for _, val := range row {
			if val >= 2 {
				result++
			}
		}
	}
	return result
}

func part1(input [][]int) int {
	var result [1000][1000]int

	for _, v := range input {
		if v[0] == v[2] {
			if v[1] < v[3] {
				for i := v[1]; i <= v[3]; i++ {
					result[i][v[0]] = result[i][v[0]] + 1
				}
			} else {
				for i := v[3]; i <= v[1]; i++ {
					result[i][v[0]] = result[i][v[0]] + 1
				}
			}
		} else if v[1] == v[3] {
			if v[0] < v[2] {
				for i := v[0]; i <= v[2]; i++ {
					result[v[1]][i] = result[v[1]][i] + 1
				}
			} else {
				for i := v[2]; i <= v[0]; i++ {
					result[v[1]][i] = result[v[1]][i] + 1
				}
			}
		}
	}

	log.Printf("%v", result)

	return countCross(result)
}

func part2(input [][]int) int {
	var result [1000][1000]int

	for _, v := range input {
		// Only horizontal or vertical
		if v[0] == v[2] {
			if v[1] < v[3] {
				for i := v[1]; i <= v[3]; i++ {
					result[i][v[0]] = result[i][v[0]] + 1
				}
			} else {
				for i := v[3]; i <= v[1]; i++ {
					result[i][v[0]] = result[i][v[0]] + 1
				}
			}
		} else if v[1] == v[3] {
			if v[0] < v[2] {
				for i := v[0]; i <= v[2]; i++ {
					result[v[1]][i] = result[v[1]][i] + 1
				}
			} else {
				for i := v[2]; i <= v[0]; i++ {
					result[v[1]][i] = result[v[1]][i] + 1
				}
			}
		}
		// TODO diagonal 45 degrees

	}

	log.Printf("%v", result)

	return countCross(result)
}

func main() {
	lines := ReadFileToStr("day5.txt")
	input := parseInput(lines)
	log.Printf("Part 1: %d", part1(input))
	log.Printf("Part 2: %d", part2(input))
}

package main

import (
	"bufio"
	"log"
	"math"
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
		xMax := int(math.Max(float64(v[0]), float64(v[2])))
		xMin := int(math.Min(float64(v[0]), float64(v[2])))
		yMax := int(math.Max(float64(v[1]), float64(v[3])))
		yMin := int(math.Min(float64(v[1]), float64(v[3])))

		if v[0] == v[2] {
			for y := yMin; y <= yMax; y++ {
				result[y][v[0]] += 1
			}
		} else if v[1] == v[3] {
			for x := xMin; x <= xMax; x++ {
				result[v[1]][x] += 1
			}
		}
	}
	return countCross(result)
}

func part2(input [][]int) int {
	var result [1000][1000]int

	for _, v := range input {
		xMax := int(math.Max(float64(v[0]), float64(v[2])))
		xMin := int(math.Min(float64(v[0]), float64(v[2])))
		yMax := int(math.Max(float64(v[1]), float64(v[3])))
		yMin := int(math.Min(float64(v[1]), float64(v[3])))

		diffX := int(math.Abs(float64(xMax - xMin)))

		if v[0] == v[2] {
			for y := yMin; y <= yMax; y++ {
				result[y][v[0]] += 1
			}
		} else if v[1] == v[3] {
			for x := xMin; x <= xMax; x++ {
				result[v[1]][x] += 1
			}
		} else {
			// Diagonal
			coeffX, coeffY := 1, 1
			if v[0] > v[2] {
				coeffX = -1
			}
			if v[1] > v[3] {
				coeffY = -1
			}
			for i := 0; i <= diffX; i++ {
				result[coeffY*i+v[1]][coeffX*i+v[0]] += 1
			}
		}
	}
	return countCross(result)
}

func main() {
	lines := ReadFileToStr("day5.txt")
	input := parseInput(lines)
	log.Printf("Part 1: %d", part1(input))
	log.Printf("Part 2: %d", part2(input))
}

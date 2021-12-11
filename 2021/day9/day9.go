package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func ParseNums(fileName string) [][]int {
	file, err := os.Open(fileName)

	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	var numbers [][]int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		var row []int
		row = append(row, 9)
		for _, val := range line {
			num, err := strconv.Atoi(string(val))
			if err != nil {
				log.Fatalf("readLines: %s", err)
			}
			row = append(row, num)
		}
		row = append(row, 9)
		numbers = append(numbers, row)
	}
	var fullNineRow []int
	for i := 0; i < len(numbers[0]); i++ {
		fullNineRow = append(fullNineRow, 9)
	}
	// Adds a row of 9 to top and bottom
	numbers = append([][]int{fullNineRow}, numbers...)
	numbers = append(numbers, fullNineRow)
	return numbers
}

type coord struct {
	x, y int
}

func dfs(volcano [][]int, start coord) int {
	seen := make(map[coord]bool)
	stack := []coord{start}
	posToCheck := []coord{
		{x: 0, y: 1},
		{x: 1, y: 0},
		{x: 0, y: -1},
		{x: -1, y: 0},
	}
	var basinSize int
	for len(stack) > 0 {
		head := stack[0]
		stack = stack[1:]
		for _, pos := range posToCheck {
			currPoint := head
			currPoint.x += pos.x
			currPoint.y += pos.y
			if seen[currPoint] {
				continue
			}
			seen[currPoint] = true
			v := volcano[currPoint.y][currPoint.x]
			if v < 9 {
				basinSize++
				stack = append(stack, currPoint)
			}
		}
	}
	return basinSize
}

func part1(volcano [][]int) int {
	var riskLevel int
	posToCheck := []coord{
		{x: 0, y: 1},
		{x: 1, y: 0},
		{x: 0, y: -1},
		{x: -1, y: 0},
	}
	for col := 1; col < len(volcano[0])-1; col++ {
		for row := 1; row < len(volcano)-1; row++ {
			var adjacentPoints, lowerPoints int
			for _, pos := range posToCheck {
				adjacentPoints++
				currentPos := coord{x: col, y: row}
				currentPos.x += pos.x
				currentPos.y += pos.y
				if volcano[row][col] < volcano[currentPos.y][currentPos.x] {
					lowerPoints++
				}
			}
			if adjacentPoints == lowerPoints {
				riskLevel += 1 + volcano[row][col]
			}
		}
	}
	return riskLevel
}

func part2(volcano [][]int) int {
	var basins []int
	posToCheck := []coord{
		{x: 0, y: 1},
		{x: 1, y: 0},
		{x: 0, y: -1},
		{x: -1, y: 0},
	}
	for col := 1; col < len(volcano[0])-1; col++ {
		for row := 1; row < len(volcano)-1; row++ {
			var adjacentPoints, lowerPoints int
			for _, pos := range posToCheck {
				adjacentPoints++
				currentPos := coord{x: col, y: row}
				currentPos.x += pos.x
				currentPos.y += pos.y
				if volcano[row][col] < volcano[currentPos.y][currentPos.x] {
					lowerPoints++
				}
			}
			if adjacentPoints == lowerPoints {
				basins = append(basins, dfs(volcano, coord{x: col, y: row}))
			}
		}
	}
	sort.Ints(basins)
	top3Basins := basins[len(basins)-3:]
	total := 1
	for _, size := range top3Basins {
		total *= size
	}
	return total
}

func main() {
	// Init volcano
	volcano := ParseNums("day9.txt")
	fmt.Printf("Part1: %d\n", part1(volcano))
	fmt.Printf("Part2: %d\n", part2(volcano))
}

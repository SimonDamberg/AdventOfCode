package main

import (
	"bufio"
	"log"
	"os"
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
		for _, val := range line {
			num, err := strconv.Atoi(string(val))
			if err != nil {
				log.Fatalf("readLines: %s", err)
			}
			row = append(row, num)
		}
		numbers = append(numbers, row)
	}
	return numbers
}

type coord struct {
	x, y int
}

var totalFlashes int

func flash(pos coord, numbers [][]int, maxX int, maxY int) {
	posToCheck := []coord{
		{x: 0, y: 1},
		{x: 0, y: -1},
		{x: 1, y: 1},
		{x: 1, y: 0},
		{x: 1, y: -1},
		{x: -1, y: 1},
		{x: -1, y: 0},
		{x: -1, y: -1},
	}

	// Mark current pos as flashed
	totalFlashes++
	numbers[pos.y][pos.x] = -1

	for _, delta := range posToCheck {
		currPoint := pos
		currPoint.x += delta.x
		currPoint.y += delta.y

		// Check if point is in bounds
		if 0 <= currPoint.x && currPoint.x < maxX && 0 <= currPoint.y && currPoint.y < maxY {
			if numbers[currPoint.y][currPoint.x] != -1 {
				numbers[currPoint.y][currPoint.x]++
				if numbers[currPoint.y][currPoint.x] >= 10 {
					flash(currPoint, numbers, maxX, maxY)
				}
			}
		}
	}
}

func day11(numbers [][]int) {
	step := 0
	maxX := len(numbers[0])
	maxY := len(numbers)
	for {
		step++

		// Make all charge 1 energy
		for row := range numbers {
			for col := range numbers[row] {
				numbers[row][col]++
			}
		}

		// Check for flashing squid
		for row := range numbers {
			for col := range numbers[row] {
				if numbers[row][col] == 10 {
					currentPos := coord{x: col, y: row}
					flash(currentPos, numbers, maxX, maxY)
				}
			}
		}

		complete := true

		// Make all flashed squids 0
		for row := range numbers {
			for col := range numbers[row] {
				if numbers[row][col] == -1 {
					numbers[row][col] = 0
				} else {
					complete = false // Complete if all squids flash at the same time
				}
			}
		}

		if step == 100 {
			log.Printf("Part 1: %v", totalFlashes)
		}
		if complete {
			log.Printf("Part 2: %v", step)
			break
		}
	}
}

func main() {
	numbers := ParseNums("day11.txt")
	day11(numbers)
}

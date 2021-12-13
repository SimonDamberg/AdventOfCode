package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type FileParse struct {
	folds   []string
	numbers [][]int
}

func ReadFileToStr(fileName string) FileParse {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	var numbers [][]int
	var folds []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		val := scanner.Text()
		if len(val) > 0 { // Skip empty line
			if val[0] == 'f' { // A fold
				folds = append(folds, val)
			} else {
				coords := strings.Split(val, ",")
				x, _ := strconv.Atoi(coords[0])
				y, _ := strconv.Atoi(coords[1])
				numbers = append(numbers, []int{x, y})
			}
		}
	}
	return FileParse{folds: folds, numbers: numbers}
}

// Note: Maybe not the fastest way to iterate through every fold, but it works
func removeDuplicates(numbers [][]int) [][]int {
	var uniqueNumbers [][]int
	for _, number := range numbers {
		found := false
		for _, uniqueNumber := range uniqueNumbers {
			if number[0] == uniqueNumber[0] && number[1] == uniqueNumber[1] {
				found = true
				break
			}
		}
		if !found {
			uniqueNumbers = append(uniqueNumbers, number)
		}
	}
	return uniqueNumbers
}

func day13(fp FileParse) {
	folds := fp.folds
	numbers := fp.numbers
	smallestX := 1000000
	smallestY := 1000000
	for i := 0; i < len(folds); i++ { // Only first folds
		var foldVal int
		fold := folds[i]
		if strings.Contains(fold, "x") {
			foldVal, _ = strconv.Atoi(strings.Split(fold, "x=")[1])
			if foldVal < smallestX {
				smallestX = foldVal - 1
			}
			for _, number := range numbers {
				if number[0] > foldVal {
					difference := number[0] - foldVal
					number[0] = foldVal - difference
				}
			}
		} else {
			foldVal, _ = strconv.Atoi(strings.Split(fold, "y=")[1])
			if foldVal < smallestY {
				smallestY = foldVal - 1
			}
			for _, number := range numbers {
				if number[1] > foldVal {
					difference := number[1] - foldVal
					number[1] = foldVal - difference
				}
			}
		}
		numbers = removeDuplicates(numbers)
		if i == 0 { // First fold, Part 1
			log.Printf("Part 1: %d", len(numbers))
		}
	}
	// Init string grid filled with blank spaces
	grid := make([]string, smallestY+1)
	for i := 0; i < len(grid); i++ {
		grid[i] = strings.Repeat(" ", smallestX+1)
	}

	for _, number := range numbers {
		// Replace char at position with #
		col, row := number[0], number[1]
		newString := grid[row][:col] + "#" + grid[row][col+1:]
		grid = append(grid[:row], append([]string{newString}, grid[row+1:]...)...)
	}

	log.Printf("=============== Part 2 ===============")

	for _, row := range grid {
		log.Printf("%s", row)
	}
}

func main() {
	lines := ReadFileToStr("day13.txt")
	day13(lines)
}

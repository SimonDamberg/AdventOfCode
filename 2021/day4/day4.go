package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

// Helper function to parse a list of strings into list of int
func sliceAtoi(sa []string) ([]int, error) {
	si := make([]int, 0, len(sa))
	for _, a := range sa {
		i, err := strconv.Atoi(a)
		if err != nil {
			return si, err
		}
		si = append(si, i)
	}
	return si, nil
}

func parseBoards(boards []string) [][]int {
	var parsedBoards [][]int
	for i := 1; i < len(boards); i += 6 {
		var currentBoard []int
		for j := i; j < i+5; j++ {

			// Remove empty spaces before single digits
			currentLine := strings.Split(boards[j], " ")
			for i2, v := range currentLine {
				if v == "" {
					currentLine = append(currentLine[:i2], currentLine[i2+1:]...)
				}
			}

			// Parse row into int and save into current board
			intBoard, _ := sliceAtoi(currentLine)
			currentBoard = append(currentBoard, intBoard...)
		}
		parsedBoards = append(parsedBoards, currentBoard)
	}
	return parsedBoards
}

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

func checkBoard(number int, board []int) []int {
	for i, v := range board {
		if number == v {
			board[i] = 100
		}
	}
	return board
}

// Always 5x5 squares
func checkWin(boards [][]int) (int, []int, bool) {
	// Check rows
	for loc, board := range boards {
		for i := 0; i < len(board); i += 5 {
			if board[i] == 100 && board[i+1] == 100 && board[i+2] == 100 && board[i+3] == 100 && board[i+4] == 100 {
				return loc, board, true
			}
		}
		// Check columns
		for i := 0; i < 5; i++ {
			if board[i] == 100 && board[i+5] == 100 && board[i+10] == 100 && board[i+15] == 100 && board[i+20] == 100 {
				return loc, board, true
			}
		}
	}
	return -1, nil, false
}

func sumUnmarkedNums(board []int) int {
	var sum int
	for _, v := range board {
		if v != 100 {
			sum += v
		}
	}
	return sum
}

func part1(numbers []int, boards [][]int) int {
	for len(boards) > 0 {
		for _, number := range numbers {
			for i, board := range boards {
				boards[i] = checkBoard(number, board)
			}

			// Check if column or row is 100 in all places
			if _, winner, won := checkWin(boards); won {
				sum := sumUnmarkedNums(winner)
				return sum * number
			}

		}
	}
	return 0
}

func part2(numbers []int, boards [][]int) int {
	lastScore := 0
	for len(boards) > 0 {
		for _, number := range numbers {
			for i, board := range boards {
				boards[i] = checkBoard(number, board)
			}

			// Check if column or row is 100 in all places
			if loc, winner, won := checkWin(boards); won {
				lastScore = sumUnmarkedNums(winner) * number
				boards = append(boards[:loc], boards[loc+1:]...)
				break
			}
		}
	}
	return lastScore
}

func main() {
	lines := ReadFileToStr("day4.txt")
	numbers, _ := sliceAtoi(strings.Split(lines[0], ","))
	boards := parseBoards(lines[1:])

	// Memory is shared, copying before does not work :(
	log.Printf("Part 1: %d", part1(numbers, boards))
	//log.Printf("Part 2: %d", part2(numbers, boards))
}

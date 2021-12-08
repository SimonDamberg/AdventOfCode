package main

import (
	"bufio"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func parseInput(fileName string) [][]string {
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
	var parsedInputs []string
	var parsedOutputs []string
	for _, line := range lines {
		splitString := strings.Split(line, " | ")
		parsedInputs = append(parsedInputs, splitString[0])
		parsedOutputs = append(parsedOutputs, splitString[1])
	}
	var parsedLines [][]string
	parsedLines = append(parsedLines, parsedInputs, parsedOutputs)
	return parsedLines
}

func part1(outputs []string) int {
	amountToNum := map[int]int{
		2: 1,
		3: 7,
		4: 4,
		7: 8,
	}
	var sum int
	for _, output := range outputs {
		for _, line := range strings.Split(output, " ") {
			if _, ok := amountToNum[len(line)]; ok {
				sum++
			}
		}
	}
	return sum
}

func getEasyNumbers(remainingPatterns []string, easyNumbers map[int]string) []string {
	for i := 0; i < len(remainingPatterns); i++ {
		number := remainingPatterns[i]
		switch len(number) {
		case 2:
			easyNumbers[1] = number
			remainingPatterns = append(remainingPatterns[:i], remainingPatterns[i+1:]...)
			i--
		case 3:
			easyNumbers[7] = number
			remainingPatterns = append(remainingPatterns[:i], remainingPatterns[i+1:]...)
			i--
		case 4:
			easyNumbers[4] = number
			remainingPatterns = append(remainingPatterns[:i], remainingPatterns[i+1:]...)
			i--
		case 7:
			easyNumbers[8] = number
			remainingPatterns = append(remainingPatterns[:i], remainingPatterns[i+1:]...)
			i--
		}
	}
	return remainingPatterns
}

func commonChars(number1 string, number2 string) int {
	var common string
	for i := 0; i < len(number1); i++ {
		for j := 0; j < len(number2); j++ {
			if string(number1[i]) == string(number2[j]) {
				common += string(number1[i])
			}
		}
	}
	return len(common)
}

func getOutputNumber(patterns map[int]string, output string) int {
	number := ""
	for _, line := range strings.Split(output, " ") {
		for i, pattern := range patterns {
			// Check if pattern is the same as line
			if SortString(pattern) == SortString(line) {
				number += strconv.Itoa(i)
			}
		}
	}
	num, _ := strconv.Atoi(number)
	return num
}

func SortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func part2(parsedInput [][]string) int {
	var sum int
	for j, line := range parsedInput[0] {
		remainingPatterns := strings.Split(line, " ")
		patterns := map[int]string{}
		remainingPatterns = getEasyNumbers(remainingPatterns, patterns) // Sets up map of easy numbers 1 4 7 8

		for len(patterns) < 10 { // Loop until all patterns are found
			for i := 0; i < len(remainingPatterns); i++ {
				num := remainingPatterns[i]

				switch len(num) {
				case 6: // Numbers 0, 6, 9 have length 6
					if commonChars(patterns[4], num) == 4 {
						// 4 common chars with 4 => 9
						patterns[9] = num
					} else if commonChars(patterns[7], num) == 2 && num != patterns[9] && len(patterns[9]) > 0 {
						// 2 common chars with 7 and not 9 => 6
						patterns[6] = num
					} else if num != patterns[9] && num != patterns[6] && len(patterns[6]) > 0 && len(patterns[9]) > 0 {
						// Not 9 or 6 => 0
						patterns[0] = num
					}
				case 5: // 5, 3, 2
					if commonChars(patterns[6], num) == 5 {
						// 5 common chars with 6 => 5
						patterns[5] = num
					} else if commonChars(patterns[4], num) == 3 && num != patterns[5] && len(patterns[5]) > 0 {
						// 3 common chars with 4 and not 5 => 3
						patterns[3] = num
					} else if num != patterns[5] && num != patterns[3] && len(patterns[3]) > 0 && len(patterns[5]) > 0 {
						// Not 5 or 3 => 2
						patterns[2] = num
					}
				}
			}
		}
		sum += getOutputNumber(patterns, parsedInput[1][j])
	}
	return sum
}

func main() {
	lines := parseInput("day8.txt")
	outputs := lines[1]
	log.Printf("Part 1: %d", part1(outputs))
	log.Printf("Part 2: %d", part2(lines))
}

// 0:      1:      2:      3:      4:
// 	aaaa    ....    aaaa    aaaa    ....
// b    c  .    c  .    c  .    c  b    c
// b    c  .    c  .    c  .    c  b    c
// ....    ....    dddd    dddd    dddd
// e    f  .    f  e    .  .    f  .    f
// e    f  .    f  e    .  .    f  .    f
// 	gggg    ....    gggg    gggg    ....

//  5:      6:      7:      8:      9:
// 	aaaa    aaaa    aaaa    aaaa    aaaa
// b    .  b    .  .    c  b    c  b    c
// b    .  b    .  .    c  b    c  b    c
// 	dddd    dddd    ....    dddd    dddd
// .    f  e    f  .    f  e    f  .    f
// .    f  e    f  .    f  e    f  .    f
// 	gggg    gggg    ....    gggg    gggg

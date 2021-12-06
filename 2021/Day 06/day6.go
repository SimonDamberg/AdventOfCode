package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func ParseNums(fileName string) []int {
	file, err := os.Open(fileName)
	defer file.Close()

	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	var numbers []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		for _, val := range strings.Split(line, ",") {
			num, err := strconv.Atoi(val)
			if err != nil {
				log.Fatalf("readLines: %s", err)
			}
			numbers = append(numbers, num)
		}
	}
	return numbers
}

func getTotalFish(fish []int) int {
	total := 0
	for _, val := range fish {
		total += val
	}
	return total
}

func main() {

	// Init fish
	startingNums := ParseNums("day6.txt")
	fish := make([]int, len(startingNums))
	for _, v := range startingNums {
		fish[v]++
	}

	for i := 0; i < 256; i++ {
		fishToBreed := fish[0] // Remember fish at 0 days
		fish = fish[1:]        // 'Pop' fish at 0 days
		fish[6] += fishToBreed // Add fish to 6th day
		fish[8] += fishToBreed // Add fish to 8th day
		if i == 79 {
			// Print result for part 1 if we're on 80th iteration
			fmt.Printf("Part1: %d\n", getTotalFish(fish))
		}
	}
	fmt.Printf("Part2: %d\n", getTotalFish(fish))
}

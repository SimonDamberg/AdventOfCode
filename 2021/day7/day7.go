package main

import (
	"bufio"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func ParseNums(fileName string) []int {
	file, err := os.Open(fileName)
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

func getPossibleLocations(numbers []int) []int {
	possibleLocations := make([]int, 2)
	possibleLocations[0] = numbers[0]
	possibleLocations[1] = numbers[0]
	for _, v := range numbers {
		if v < possibleLocations[0] {
			possibleLocations[0] = v
		} else if v > possibleLocations[1] {
			possibleLocations[1] = v
		}
	}

	return possibleLocations
}

func checkFuelCostPart1(numbers []int, location int) int {
	var totalFuel int
	for _, v := range numbers {
		cost := math.Abs(float64(location - v))
		totalFuel += int(cost)
	}
	return totalFuel
}

func checkFuelCostPart2(numbers []int, location int) int {
	var totalFuel int
	for _, v := range numbers {
		steps := math.Abs(float64(location - v))
		for i := 0; i <= int(steps); i++ {
			totalFuel += 1 * i
		}
	}
	return totalFuel
}

func main() {
	crabs := ParseNums("day7.txt")
	possibleLocations := getPossibleLocations(crabs)
	lowestCostPart1 := math.MaxInt32
	lowestCostPart2 := math.MaxInt32
	for i := possibleLocations[0]; i <= possibleLocations[1]; i++ {
		cost1 := checkFuelCostPart1(crabs, i)
		cost2 := checkFuelCostPart2(crabs, i)
		if cost1 < lowestCostPart1 {
			lowestCostPart1 = cost1
		}
		if cost2 < lowestCostPart2 {
			lowestCostPart2 = cost2
		}
	}
	log.Printf("Part 1: %d", lowestCostPart1)
	log.Printf("Part 2: %d", lowestCostPart2)
}

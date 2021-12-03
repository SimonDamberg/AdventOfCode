package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
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

func part2(lines []string) int64 {
	oxygen := make([]string, len(lines))
	scrubber := make([]string, len(lines))
	copy(oxygen, lines)
	copy(scrubber, lines)
	// Oxygen
	for {
		for i := 0; i < len(oxygen[0]); i++ {
			ones, zeros := 0, 0

			for j := 0; j < len(oxygen); j++ {
				if oxygen[j][i] == '1' {
					ones++
				} else {
					zeros++
				}
			}
			lenghtOfOxygen := len(oxygen)
			if ones >= zeros {
				for j := 0; j < lenghtOfOxygen; j++ {
					if oxygen[j][i] == '0' {
						// Remove element from array
						oxygen = append(oxygen[:j], oxygen[j+1:]...)
						j--
						lenghtOfOxygen = len(oxygen)
					}
				}
			} else {
				for j := 0; j < lenghtOfOxygen; j++ {
					if oxygen[j][i] == '1' {
						// Remove element from array
						oxygen = append(oxygen[:j], oxygen[j+1:]...)
						j--
						lenghtOfOxygen = len(oxygen)
					}
				}
			}
			if len(oxygen) == 1 {
				break
			}
		}
		if len(oxygen) == 1 {
			break
		}
	}

	// Scrubber
	for {
		for i := 0; i < len(scrubber[0]); i++ {
			ones, zeros := 0, 0

			for j := 0; j < len(scrubber); j++ {
				if scrubber[j][i] == '1' {
					ones++
				} else {
					zeros++
				}
			}
			lenghtOfScrubber := len(scrubber)
			if ones >= zeros {
				for j := 0; j < lenghtOfScrubber; j++ {
					if scrubber[j][i] == '1' {
						// Remove element from array
						scrubber = append(scrubber[:j], scrubber[j+1:]...)
						j--
						lenghtOfScrubber = len(scrubber)
					}
				}
			} else {
				for j := 0; j < lenghtOfScrubber; j++ {
					if scrubber[j][i] == '0' {
						// Remove element from array
						scrubber = append(scrubber[:j], scrubber[j+1:]...)
						j--
						lenghtOfScrubber = len(scrubber)
					}
				}
			}
			if len(scrubber) == 1 {
				break
			}
		}
		if len(scrubber) == 1 {
			break
		}
	}
	oxygenInt, _ := strconv.ParseInt(oxygen[0], 2, 64)
	scrubberInt, _ := strconv.ParseInt(scrubber[0], 2, 64)
	return oxygenInt * scrubberInt
}
func main() {
	lines := ReadFileToStr("day3.txt")
	log.Printf("Part 2: %d", part2(lines))
}

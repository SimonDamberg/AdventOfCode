package main

import (
	"bufio"
	"log"
	"os"
	"strings"
	"unicode"
)

func IsLower(s string) bool {
	for _, c := range s {
		if !unicode.IsLower(c) && unicode.IsLetter(c) {
			return false
		}
	}
	return true
}

func ParseFile(fileName string) map[string][]string {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	var paths = make(map[string][]string)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		val := strings.Split(scanner.Text(), "-")

		// Edge cases with start since you cannot go to start
		if val[0] == "start" {
			paths[val[0]] = append(paths[val[0]], val[1])
			continue
		} else if val[1] == "start" {
			paths[val[1]] = append(paths[val[1]], val[0])
			continue
		}

		// Edge cases with end since you cannot go from end
		if val[0] == "end" {
			paths[val[1]] = append(paths[val[1]], val[0])
			continue
		} else if val[1] == "end" {
			paths[val[0]] = append(paths[val[0]], val[1])
			continue
		}

		// Otherwise, add both directions
		paths[val[1]] = append(paths[val[1]], val[0])
		paths[val[0]] = append(paths[val[0]], val[1])

	}
	return paths
}

// Modified DFS
func dfs(paths map[string][]string, visited map[string]int, startPos string, visitSmallOnce bool) [][]string {
	var allPaths [][]string
	possiblePaths := paths[startPos]
	for _, path := range possiblePaths {

		// If we are at the end, add end and countinue to other options
		if path == "end" {
			allPaths = append(allPaths, []string{"end"})
			continue
		}

		// Check if it is a small cave that have been visited at least once
		hasVisited := visitSmallOnce
		if IsLower(path) && visited[path] >= 1 {
			if hasVisited { // If we only should visit once
				continue
			} else { // If we should visit more than once
				hasVisited = true
			}
		}

		// Make a copy of visited to not overwrite
		copyOfVisited := make(map[string]int)
		for k, v := range visited {
			copyOfVisited[k] = v
		}
		copyOfVisited[path]++

		pathsToAdd := dfs(paths, copyOfVisited, path, hasVisited)
		for _, pathToAdd := range pathsToAdd {
			allPaths = append(allPaths, append([]string{path}, pathToAdd...))
		}

	}
	return allPaths
}

func main() {
	paths := ParseFile("day12.txt")
	log.Printf("Part 1: %v", len(dfs(paths, map[string]int{}, "start", true)))
	log.Printf("Part 2: %v", len(dfs(paths, map[string]int{}, "start", false)))

}

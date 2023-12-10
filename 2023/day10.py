import math
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 10 # CHANGE THIS
# ------------------ #

def get_start_coords(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                return (x,y)

pipe_to_dir = {
    "|": ["n", "s"], # north, south
    "-": ["e", "w"], # east, west
    "L": ["n", "e"], # north, east
    "J": ["n", "w"], # north, west
    "7": ["s", "w"], # south, west
    "F": ["s", "e"], # south, east
    ".": [], # no direction
}
dirs = {
    "n": (0,-1),
    "s": (0,1),
    "e": (1,0),
    "w": (-1,0),
}
opposite = {
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e",
}

# dfs to find shortest path
def dfs(grid, start, end, from_dir):
    visited = set()
    stack = [(start, from_dir, [start])] # stack contains (current, from_dir, path)
    while stack:
        ((x,y), from_dir, path) = stack.pop()
        if (x,y) not in visited:
            if (x,y) == end:
                return path
            visited.add((x,y))
            neighbors = pipe_to_dir[grid[y][x]].copy()
            if from_dir in neighbors:
                neighbors.remove(from_dir) # if we came from a direction, we can't go back
            for dir in neighbors:
                dx, dy = dirs[dir]
                if (x+dx,y+dy) not in visited:
                    stack.append(((x+dx,y+dy), opposite[dir], path + [(x+dx,y+dy)]))
    return []
    

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 4
    answer = 0
    grid = [list(line) for line in input.splitlines()]
    start = get_start_coords(grid)
    
    for dir in ["n", "s", "e", "w"]:
        dx, dy = dirs[dir]
        print(f"dir: {dir}")
        path = dfs(grid, (start[0]+dx, start[1]+dy), start, opposite[dir])
        if len(path) > 0:
            answer = len(path) // 2 # farthest point is half of the loop length
            break
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    
    # get path of loop from part 1
    grid = [list(line) for line in input.splitlines()]
    start = get_start_coords(grid)
    for dir in ["n", "s", "e", "w"]:
        dx, dy = dirs[dir]
        print(f"dir: {dir}")
        loop = dfs(grid, (start[0]+dx, start[1]+dy), start, opposite[dir])
        if len(loop) > 0:
            break

    # make the grid into 3x3 squares to flood fill and find enclosed areas
    big_grid = {}
    for y, line in enumerate(input.splitlines()):
        for x, pipe in enumerate(line):
            if (x,y) not in loop:
                # if not in the loop, insert 3x3 grid of "0"
                big_grid[(x*3 + 0,y*3 + 0)] = "0"
                big_grid[(x*3 + 1,y*3 + 0)] = "0"
                big_grid[(x*3 + 2,y*3 + 0)] = "0"
                big_grid[(x*3 + 0,y*3 + 1)] = "0"
                big_grid[(x*3 + 1,y*3 + 1)] = "0"
                big_grid[(x*3 + 2,y*3 + 1)] = "0"
                big_grid[(x*3 + 0,y*3 + 2)] = "0"
                big_grid[(x*3 + 1,y*3 + 2)] = "0"
                big_grid[(x*3 + 2,y*3 + 2)] = "0"
            else:
                # else, insert shape of pipe in 3x3 scale
                match pipe:
                    case "S":
                        big_grid[(x*3 + 0,y*3 + 0)] = "+"
                        big_grid[(x*3 + 1,y*3 + 0)] = "+"
                        big_grid[(x*3 + 2,y*3 + 0)] = "+"
                        big_grid[(x*3 + 0,y*3 + 1)] = "+"
                        big_grid[(x*3 + 1,y*3 + 1)] = "+"
                        big_grid[(x*3 + 2,y*3 + 1)] = "+"
                        big_grid[(x*3 + 0,y*3 + 2)] = "+"
                        big_grid[(x*3 + 1,y*3 + 2)] = "+"
                        big_grid[(x*3 + 2,y*3 + 2)] = "+"
                    case "-":
                        big_grid[(x*3 + 0,y*3 + 0)] = "0"
                        big_grid[(x*3 + 1,y*3 + 0)] = "0"
                        big_grid[(x*3 + 2,y*3 + 0)] = "0"
                        big_grid[(x*3 + 0,y*3 + 1)] = "#"
                        big_grid[(x*3 + 1,y*3 + 1)] = "#"
                        big_grid[(x*3 + 2,y*3 + 1)] = "#"
                        big_grid[(x*3 + 0,y*3 + 2)] = "0"
                        big_grid[(x*3 + 1,y*3 + 2)] = "0"
                        big_grid[(x*3 + 2,y*3 + 2)] = "0"
                    case "|":
                        big_grid[(x*3 + 0,y*3 + 0)] = "0"
                        big_grid[(x*3 + 1,y*3 + 0)] = "#"
                        big_grid[(x*3 + 2,y*3 + 0)] = "0"
                        big_grid[(x*3 + 0,y*3 + 1)] = "0"
                        big_grid[(x*3 + 1,y*3 + 1)] = "#"
                        big_grid[(x*3 + 2,y*3 + 1)] = "0"
                        big_grid[(x*3 + 0,y*3 + 2)] = "0"
                        big_grid[(x*3 + 1,y*3 + 2)] = "#"
                        big_grid[(x*3 + 2,y*3 + 2)] = "0"
                    case "L":
                        big_grid[(x*3 + 0,y*3 + 0)] = "0"
                        big_grid[(x*3 + 1,y*3 + 0)] = "#"
                        big_grid[(x*3 + 2,y*3 + 0)] = "0"
                        big_grid[(x*3 + 0,y*3 + 1)] = "0"
                        big_grid[(x*3 + 1,y*3 + 1)] = "#"
                        big_grid[(x*3 + 2,y*3 + 1)] = "#"
                        big_grid[(x*3 + 0,y*3 + 2)] = "0"
                        big_grid[(x*3 + 1,y*3 + 2)] = "0"
                        big_grid[(x*3 + 2,y*3 + 2)] = "0"
                    case "J":
                        big_grid[(x*3 + 0,y*3 + 0)] = "0"
                        big_grid[(x*3 + 1,y*3 + 0)] = "#"
                        big_grid[(x*3 + 2,y*3 + 0)] = "0"
                        big_grid[(x*3 + 0,y*3 + 1)] = "#"
                        big_grid[(x*3 + 1,y*3 + 1)] = "#"
                        big_grid[(x*3 + 2,y*3 + 1)] = "0"
                        big_grid[(x*3 + 0,y*3 + 2)] = "0"
                        big_grid[(x*3 + 1,y*3 + 2)] = "0"
                        big_grid[(x*3 + 2,y*3 + 2)] = "0"
                    case "7":
                        big_grid[(x*3 + 0,y*3 + 0)] = "0"
                        big_grid[(x*3 + 1,y*3 + 0)] = "0"
                        big_grid[(x*3 + 2,y*3 + 0)] = "0"
                        big_grid[(x*3 + 0,y*3 + 1)] = "#"
                        big_grid[(x*3 + 1,y*3 + 1)] = "#"
                        big_grid[(x*3 + 2,y*3 + 1)] = "0"
                        big_grid[(x*3 + 0,y*3 + 2)] = "0"
                        big_grid[(x*3 + 1,y*3 + 2)] = "#"
                        big_grid[(x*3 + 2,y*3 + 2)] = "0"
                    case "F":
                        big_grid[(x*3 + 0,y*3 + 0)] = "0"
                        big_grid[(x*3 + 1,y*3 + 0)] = "#"
                        big_grid[(x*3 + 2,y*3 + 0)] = "0"
                        big_grid[(x*3 + 0,y*3 + 1)] = "0"
                        big_grid[(x*3 + 1,y*3 + 1)] = "#"
                        big_grid[(x*3 + 2,y*3 + 1)] = "#"
                        big_grid[(x*3 + 0,y*3 + 2)] = "0"
                        big_grid[(x*3 + 1,y*3 + 2)] = "#"
                        big_grid[(x*3 + 2,y*3 + 2)] = "0"

    # set top corner to . and flood fill to find enclosed areas
    big_grid[(0, 0)] = "."
    queue = [(0,1), (1,0), (1,1)]
    while queue:
        (x,y) = queue.pop()
        if big_grid[(x,y)] == "0":
            for neighbor in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]:
                if neighbor in big_grid and big_grid[neighbor] == ".":
                    big_grid[(x,y)] = "."
                if neighbor in big_grid and big_grid[neighbor] == "0":
                    queue.append(neighbor)

    
    TRUE_ANSWER = 4
    answer = 0
    # loop through original resolution grid and check if all 9 in 3x3 square are 0
    for y, line in enumerate(input.splitlines()):
        for x, pipe in enumerate(line):
            if big_grid[(x*3 + 0,y*3 + 0)] == "0" and big_grid[(x*3 + 1,y*3 + 0)] == "0" and big_grid[(x*3 + 2,y*3 + 0)] == "0" and \
            big_grid[(x*3 + 0,y*3 + 1)] == "0" and big_grid[(x*3 + 1,y*3 + 1)] == "0" and big_grid[(x*3 + 2,y*3 + 1)] == "0" and \
            big_grid[(x*3 + 0,y*3 + 2)] == "0" and big_grid[(x*3 + 1,y*3 + 2)] == "0" and big_grid[(x*3 + 2,y*3 + 2)] == "0":
                answer += 1

    if test_case:
        print(f'(TEST) Part 2: {answer}')
        submit_if_correct(solve_part_2, answer, TRUE_ANSWER, DAY, 2, YEAR)
    else:
        print(f'(REAL) Part 2: {answer}')
    return answer

part1=open(f"ex_inputs/day{DAY}/1.txt","r")
solve_part_1(part1.read(), test_case=True)
part2=open(f"ex_inputs/day{DAY}/2.txt","r")
solve_part_2(part2.read(), test_case=True)
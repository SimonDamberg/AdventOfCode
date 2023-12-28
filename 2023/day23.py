from collections import defaultdict, deque
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 23 # CHANGE THIS
# ------------------ #

slope_to_delta = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

def get_longest_path(grid, start, end, part2=False):
    start = (1, 0)
    end = (len(grid[0])-2, len(grid)-1)
    stack = [(start, 0)] # (x,y,steps)
    visited = set()
    best = 0

    # DFS to find longest path to end
    while stack:
        pos, steps = stack.pop()
        if steps is None: # backtrack
            visited.remove(pos)
            continue
        if pos == end:
            #print(f"Found path of length {steps}")
            best = max(best, steps)
            continue
        if pos in visited:
            continue
        
        visited.add(pos)
        stack.append((pos, None)) # add back to stack to remove later to explore other paths

        (x, y) = pos
        if grid[y][x] == ".":
            # all neighbors
            deltas = slope_to_delta.values()
        else:
            # we are at slope, only 1 neighbor
            if part2:
                deltas = slope_to_delta.values()
            else:
                deltas = [slope_to_delta[grid[y][x]]]

        # explore all neighbors
        for (dx, dy) in deltas:
            if (x+dx, y+dy) not in visited:
                if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
                    if grid[y+dy][x+dx] != "#":
                        stack.append(((x+dx, y+dy), steps+1))
    return best

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 94
    grid = []
    for y, line in enumerate(input.splitlines()):
        row = []
        for x, char in enumerate(line):
            row.append(char)
        grid.append(row)

    answer = get_longest_path(grid, (1, 0), (len(grid[0])-2, len(grid)-1))

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 154

    grid = {}
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            grid[(x, y)] = char

    # build a graph from the grid
    nodes = defaultdict(list)
    for pos, char in grid.items():
        if char == ".":
            # all neighbors
            deltas = slope_to_delta.values()
        else:
            # we are at slope, only 1 neighbor
            deltas = [slope_to_delta[char]]
        for (dx, dy) in deltas:
            if 0 <= pos[0]+dx < len(grid[0]) and 0 <= pos[1]+dy < len(grid):
                if grid[(pos[0]+dx, pos[1]+dy)] != "#":
                    nodes[pos].append((pos[0]+dx, pos[1]+dy))
    
    answer = get_longest_path(grid, (1, 0), (len(grid[0])-2, len(grid)-1), part2=True)
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
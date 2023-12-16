from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 14 # CHANGE THIS
# ------------------ #

def rotate_grid_90_to_right(grid):
    return [list(row) for row in zip(*grid[::-1])] # python magic

def move_north(grid):
    moves = 0
    for y, row in enumerate(grid):
        if y == 0:
            continue
        for x, space in enumerate(row):
            if space == "O" and grid[y-1][x] == '.':
                grid[y][x] = '.'
                grid[y-1][x] = space
                moves += 1
    return moves

def calc_load(grid):
    load = 0
    num_rows = len(grid)
    for y, row in enumerate(grid):
        for space in row:
            if space == "O":
                load += (num_rows - y)
    return load

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 136
    grid = []
    for line in input.splitlines():
        row = []
        for space in line:
            row.append(space)
        grid.append(row)

    while move_north(grid) != 0: # move north until we can't
        pass
    answer = calc_load(grid)

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer

def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 64
    grid = []
    for line in input.splitlines():
        row = []
        for space in line:
            row.append(space)
        grid.append(row)
    
    # keep track of seen grids to check for loops
    seen = {}
    cycle = 1
    while cycle < 1000000000:
        for _ in range(4): # all 4 rotations
            while move_north(grid) != 0: # move north until we can't
                pass
            grid = rotate_grid_90_to_right(grid) # rotate grid to move next direction
        
        key = str(grid)
        if key not in seen.keys():
            seen[key] = cycle
            cycle += 1
        else: 
            # we've seen this grid before -> we can skip to the end
            # loop length is cycle - seen[key]
            print(f"Cycle length: {cycle - seen[key]}")
            cycles_to_skip = cycle - seen[key]
            cycle += (1000000000 - cycle) // cycles_to_skip * cycles_to_skip
            seen = {}
        
    answer = calc_load(grid)

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
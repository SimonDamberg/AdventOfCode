import copy
# Reversed and padded with 3 rows of 0 for easier adding
tetris_shapes = [[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
],[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
],[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
],[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
],[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
]]

with open('input.txt', "r") as f:
    seq = f.read().strip()

def can_move_right(grid):
    # Check if 0 to the right of all 1s
    for i in range(len(grid)):
        if grid[i][-1] == 1:
            return False
        for j in range(len(grid[i])-1):
            if grid[i][j] == 1 and grid[i][j+1] == 2:
                return False
    return True

def can_move_left(grid):
    # Check if 0 to the left of all 1s
    for i in range(len(grid)):
        if grid[i][0] == 1:
            return False
        for j in range(1, len(grid[i])):
            if grid[i][j] == 1 and grid[i][j-1] == 2:
                return False
    return True

def can_move_down(grid):
    # Check if 0 below all 1s
    for i in range(len(grid)-1):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and grid[i+1][j] == 2:
                return False
    return True

def print_grid(grid):
    for n in range(len(grid)-1):
        row = grid[n]
        print("|" + "".join(["#" if x == 2 else ("@" if x == 1 else ".") for x in row])+ "|")
    print("+-------+")

def tetris(max_cycles):
    grid = [[2 for _ in range(7)]] # Init grid with only floor
    height = 0
    curr_spawn_idx = 0
    curr_seq_idx = 0
    cache = dict()
    n = 0
    while n < max_cycles:
        n += 1

        # Hash current top 20 rows, next piece and next sequence to find repeating cycles
        curr_hash = (tuple([tuple(row) for row in grid[:20]]), curr_spawn_idx, curr_seq_idx)
        if curr_hash in cache:
            # Found cycle! Skip ahead as far as possible
            cycle_start_height, cycle_start_n = cache[curr_hash]
            d_height = height - cycle_start_height
            d_cycles = n - cycle_start_n
            repeats = (max_cycles - n) // d_cycles
            height += d_height * repeats
            n += d_cycles * repeats
        else:
            cache[curr_hash] = (height, n)

        curr_spawn = copy.deepcopy(tetris_shapes[curr_spawn_idx])
        curr_spawn_idx = (curr_spawn_idx + 1) % len(tetris_shapes)
        # Spawn new tetris piece
        for row in curr_spawn:
            grid.insert(0, row)

        while True:
            # Perform sequence
            if seq[curr_seq_idx] == "<":
                # Move all 1s to left if possible
                if can_move_left(grid):
                    for row in grid:
                        for i in range(1, len(row)):
                            if row[i] == 1:
                                row[i-1] = 1
                                row[i] = 0
            elif seq[curr_seq_idx] == ">":
                # Move all 1s to right if possible
                if can_move_right(grid):
                    for row in grid:
                        for i in range(len(row)-2, -1, -1):
                            if row[i] == 1:
                                row[i+1] = 1
                                row[i] = 0
            
            curr_seq_idx = (curr_seq_idx + 1) % len(seq)
            
            if can_move_down(grid):
                # Move down all 1s
                for i in range(len(grid)-2, -1, -1):
                    for j in range(len(grid[i])):
                        if grid[i][j] == 1:
                            grid[i+1][j] = 1
                            grid[i][j] = 0
            else:
                # Count added height
                for row in grid:
                    if 1 in row and 2 not in row:
                        height += 1

                # Freeze all 1s
                for row in grid:
                    for i in range(len(row)):
                        if row[i] == 1:
                            row[i] = 2

                # Remove all empty row
                new_grid = []
                for row in grid[:50]: # only save top 50 rows to optimise
                    if sum(row) != 0:
                        new_grid.append(row)
                grid = new_grid
                break
    return height

print(f"Part 1: {tetris(2022)}")
print(f"Part 2: {tetris(1000000000000)}")
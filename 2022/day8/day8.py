import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()
    grid = np.zeros((len(lines[0]), len(lines)), dtype=np.int8)
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            grid[x, y] = int(lines[x][y])

visible = 2 * (grid.shape[0] + grid.shape[1] - 2)
for i in range(1, grid.shape[0] - 1):
    for j in range(1, grid.shape[1] - 1):
        height = grid[i, j]

        if np.all(grid[i, j + 1:] < height):
            visible += 1
        elif np.all(grid[i, :j] < height):
            visible += 1
        elif np.all(grid[i + 1:, j] < height):
            visible += 1
        elif np.all(grid[:i, j] < height):
            visible += 1

print(f"Part 1: {visible}")

best_scenic = -np.inf
for i in range(1, grid.shape[0]-1):
    for j in range(1, grid.shape[1]-1):
        height = grid[i, j]
        scenic = 1

        # Check both x directions
        for x_dir in (-1, 1):
            x = i + x_dir
            view = 0
            while 0 <= x < grid.shape[0]:
                view += 1
                if grid[x, j] >= height:
                    break
                x += x_dir
            scenic = scenic * view

        # Check both y directions
        for y_dir in (-1, 1):
            y = j + y_dir
            view = 0
            while 0 <= y < grid.shape[1]:
                view += 1
                if grid[i, y] >= height:
                    break
                y += y_dir
            scenic = scenic * view
        
        best_scenic = max(best_scenic, scenic)

print(f"Part 2: {best_scenic}")


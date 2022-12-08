import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()
    grid = np.zeros((len(lines[0]), len(lines)), dtype=np.int8)
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            grid[x, y] = int(lines[x][y])

visible = 2 * (grid.shape[0] + grid.shape[1] - 2) # All edges are visible by default
best_scenic = -np.inf
for i in range(1, grid.shape[0]-1):
    for j in range(1, grid.shape[1]-1):
        height = grid[i, j]

        # Part 1
        if np.any([np.all(grid[i, j + 1:] < height), np.all(grid[i, :j] < height), np.all(grid[i + 1:, j] < height), np.all(grid[:i, j] < height) > 0]):
            visible += 1

        # Part 2: Check all directions
        scenic = 1
        for x_dir, y_dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x = i + x_dir
            y = j + y_dir
            view = 0
            while 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
                view += 1
                if grid[x, y] >= height:
                    break
                x += x_dir
                y += y_dir
            scenic = scenic * view
        best_scenic = max(best_scenic, scenic)

print(f"Part 1: {visible}")
print(f"Part 2: {best_scenic}")


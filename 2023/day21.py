from submit_if_correct import submit_if_correct
import numpy as np 

YEAR = 2023 

# ------------------ #
DAY = 21 # CHANGE THIS
# ------------------ #

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 42
    answer = 0
    grid = []
    for x, line in enumerate(input.splitlines()):
        row = []
        for y, space in enumerate(line):
            if space == "S":
                start = (x, y)
                row.append(".")
            else:
                row.append(space)
        grid.append(row)

    dirs_to_check = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    pos_to_check = set([start])
    for _ in range(64):
        new_poses = set()

        for pos in pos_to_check:
            for dir in dirs_to_check:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]):
                    if grid[new_pos[0]][new_pos[1]] == ".":
                        new_poses.add(new_pos)
        pos_to_check = new_poses
    answer = len(pos_to_check)
    
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer

def solve_part_2(input):
    # -------------PART 2------------- #
    grid = []
    for x, line in enumerate(input.splitlines()):
        row = []
        for y, space in enumerate(line):
            if space == "S":
                start = (x, y)
                row.append(".")
            else:
                row.append(space)
        grid.append(row)
    
    # 26501365 = 202300 * 131 + 65 (135 is width of grid, 65 is center)
    # quadratic func is f(n), f(n+m), f(n+2m)....
    # calculate for f(65), f(65+131), f(65+(131*2))
    # then use quadratic formula to extrapolate f(202300)
    
    grid_size = len(grid)
    dirs_to_check = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    points = []
    steps_to_check = [65, 65+131, 65+(131*2)]

    # Get the number of points at each step
    for idx, steps in enumerate(steps_to_check):
        pos_to_check = set([start])
        
        for _ in range(steps):
            new_poses = set()

            for pos in pos_to_check:
                for dir in dirs_to_check:
                    new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                    modded_pos = (new_pos[0] % grid_size, new_pos[1] % grid_size) # mod grid size
                    if grid[modded_pos[0]][modded_pos[1]] == ".":
                        new_poses.add(new_pos)
            pos_to_check = new_poses

        points.append((idx, len(pos_to_check)))

    # Use quadratic formula to extrapolate f(202300)
    # Get the coefficients of the quadratic equation
    coefficients = np.polyfit(*zip(*points), 2)
    # Evaluate the quadratic equation at 202300
    answer = round(np.polyval(coefficients, 202300))

    print(f'(REAL) Part 2: {answer} (not submitted)')

part1=open(f"ex_inputs/day{DAY}/1.txt","r")
solve_part_1(part1.read(), test_case=True)
part2=open(f"ex_inputs/day{DAY}/2.txt","r")
solve_part_2(part2.read())
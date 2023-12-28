from collections import defaultdict, deque
import math

import numpy as np
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 18 # CHANGE THIS
# ------------------ #

dir_to_delta = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

# 0=R, 1=D, 2=L, 3=U
hex_dir_to_delta = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1)
}


# Shoelace formula implementation
# google "area of points given x,y coords" pog moment
# https://stackoverflow.com/a/30408825
def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 62
    pos = (0, 0)
    points_border = 0
    x_coords = []
    y_coords = []
    for line in input.splitlines():
        # U 2 (#7a21e3)
        dir, dist, colour = line.split(" ")
        dist = int(dist)
        delta = dir_to_delta[dir]
        for i in range(dist):
            pos = (pos[0] + delta[0], pos[1] + delta[1])
            points_border += 1
            x_coords.append(pos[0])
            y_coords.append(pos[1])

    points_inside = PolyArea(x_coords, y_coords)  

    # Pick's theorem
    inside_area = int((points_inside - (points_border // 2) + 1))
    answer = inside_area + points_border # inside + border

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 952408144115
    pos = (0, 0)
    points_border = 0
    x_coords = []
    y_coords = []
    for line in input.splitlines():
        _, _, hex = line.split(" ")
        dist = int(hex[2:7], 16)
        dir = int(hex[7])
        delta = hex_dir_to_delta[dir]
        for i in range(dist):
            pos = (pos[0] + delta[0], pos[1] + delta[1])
            points_border += 1
            x_coords.append(pos[0])
            y_coords.append(pos[1])

    points_inside = PolyArea(x_coords, y_coords)  

    # Pick's theorem
    inside_area = int((points_inside - (points_border // 2) + 1))
    answer = inside_area + points_border # inside + border
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
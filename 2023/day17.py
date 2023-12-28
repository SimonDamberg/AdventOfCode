import heapq
import math

import numpy as np
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 17 # CHANGE THIS
# ------------------ #


# same dir first in list
dir_to_deltas = {
    "r": [(1, 0), (0, -1), (0, 1)], # can only go up, right or down
    "l": [(-1, 0), (0, 1), (0, -1)], # can only go down, left or up
    "u": [(0, -1), (-1, 0), (1, 0)], # can only go left, up or right
    "d": [(0, 1),(1, 0),(-1, 0)], # can only go right, down or left
}

delta_to_dir = {
    (1, 0): "r",
    (-1, 0): "l",
    (0, 1): "d",
    (0, -1): "u",
}

def find_min_heat(grid, start, end, min_steps, max_steps):
    visited = set()
    queue = [(0, start, "r", 1), (0, start, "d", 1)] # stack contains (heat_loss, current, curr_dir, curr_same_dir)
    while queue:
        (heat_loss, (x,y), curr_dir, curr_same_dir) = heapq.heappop(queue) # priority queue based on heat loss
        #print(f"curr: {x,y}, dir: {curr_dir}, same_dir: {curr_same_dir}, heat_loss: {heat_loss}")
        
        # Terminating conditions
        if (x,y) == end: # reached end
            return heat_loss
        if (x,y, curr_dir, curr_same_dir) in visited: # already visited this state
            continue
        
        visited.add((x,y, curr_dir, curr_same_dir)) # mark as visited
        for (dx, dy) in dir_to_deltas[curr_dir]: # Get possible next positions
            (new_x, new_y) = (x+dx, y+dy)
            if (new_x, new_y) in grid:
                # calculate new state
                new_dir = delta_to_dir[(dx,dy)]
                new_same_dir = curr_same_dir + 1 if new_dir == curr_dir else 1 # if we're going in the same direction, increment same_dir
                new_heat_loss = heat_loss + grid[(new_x,new_y)] # add heat loss
                
                # To go to next state
                # - if this is a new direction
                #   - has to have gone at least min_steps in the same direction to be valid
                # - can't go more than max_steps in the same direction
                if (new_dir != curr_dir and curr_same_dir < min_steps) or (new_same_dir > max_steps):
                    continue
                else:
                    heapq.heappush(queue, (new_heat_loss, (new_x, new_y), new_dir, new_same_dir))
    return 0

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 102

    # parse grid into {x,y: weight}
    grid = {}
    end = (0, 0) # bottom right
    for x, line in enumerate(input.splitlines()):
        for y, space in enumerate(line):
            grid[(x, y)] = int(space)
    
    start = (0, 0)    
    end = (len(input.splitlines()[0]) - 1, len(input.splitlines()) - 1)
    answer = find_min_heat(grid, start, end, 1, 3)    

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 94

    # parse grid into {x,y: weight}
    grid = {}
    end = (0, 0) # bottom right
    for x, line in enumerate(input.splitlines()):
        for y, space in enumerate(line):
            grid[(x, y)] = int(space)
    
    start = (0, 0)    
    end = (len(input.splitlines()[0]) - 1, len(input.splitlines()) - 1)
    answer = find_min_heat(grid, start, end, 4, 10)   

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

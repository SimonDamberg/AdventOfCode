from functools import cache
import math
import re
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 5 # CHANGE THIS
# ------------------ #

def parse_input(input, part_2):
    segments = input.split("\n\n")
    seeds = [int(x) for x in re.findall(r"\d+", segments[0])]
    maps = []
    for segment in segments[1:]:
        map = []
        for line in segment.splitlines()[1:]:
            destination, source, amount = re.findall(r"\d+", line)
            if part_2:
                map.append((int(destination), int(destination)+int(amount)-1, int(source)))
            else:
                map.append((int(source), int(source)+int(amount)-1, int(destination)))
        maps.append(tuple(map))
    if part_2:
        maps.reverse()
    return seeds, tuple(maps)

@cache
def get_next_value(start_val, maps):
    map = maps[0]
    curr_val = start_val
    for key in map:
        if key[0] <= curr_val <= key[1]:
            diff = curr_val - key[0]
            curr_val = key[2] + diff
            break
    return get_next_value(curr_val, maps[1:]) if len(maps) > 1 else curr_val
    
def reversed_get_next_value(start_val, maps, seeds):
    map = maps[0]
    curr_val = start_val
    for key in map:
        if key[0] <= curr_val <= key[1]:
            diff = curr_val - key[0]
            curr_val = key[2] + diff
            break
    
    if len(maps) == 1:
        for i in range(1, len(seeds), 2):
            if seeds[i-1] <= curr_val <= seeds[i-1]+seeds[i]:
                return True
        return False
    else:
        return reversed_get_next_value(curr_val, maps[1:], seeds)

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 35
    seeds, maps = parse_input(input, False)
    answer = math.inf
    for seed in seeds:
        answer = min(answer, get_next_value(seed, maps))

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 46
    seeds, maps = parse_input(input, True)
    
    # Iterate through map backwards until you find one seed that works
    answer = 0
    while True:
        if reversed_get_next_value(answer, maps, tuple(seeds)):
            break
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
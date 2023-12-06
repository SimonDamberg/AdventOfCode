from math import sqrt
import math
import re
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 6 # CHANGE THIS
# ------------------ #

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 288
    times = [int(x) for x in re.findall(r"\d+", input.split("\n")[0])]
    records = [int(x) for x in re.findall(r"\d+", input.split("\n")[1])]
    answer = 1
    for time, record in zip(times, records):
        # dist < x*(time - x) 
        # dist < time*x - x^2
        # dist + time*x - x^2 < 0 
        # POG pq-formel -> integers between root range + 1 is the answer
        x1 = time/2 + math.sqrt(time*time/4 - (record+1))
        x2 = time/2 - math.sqrt(time*time/4 - (record+1))
        answer *= math.floor(x1) - math.ceil(x2) + 1
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 71503
    time = int("".join(re.findall(r"\d+", input.split("\n")[0])))
    record = int("".join(re.findall(r"\d+", input.split("\n")[1])))
    x1 = time/2 + math.sqrt(time*time/4 - (record+1))
    x2 = time/2 - math.sqrt(time*time/4 - (record+1))
    answer = math.floor(x1) - math.ceil(x2) + 1

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
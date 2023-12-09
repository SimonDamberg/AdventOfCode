import re
from submit_if_correct import submit_if_correct
YEAR = 2023

# ------------------ #
DAY = 9  # CHANGE THIS
# ------------------ #

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 114
    answer = 0
    for line in input.splitlines():
        line = [int(x) for x in line.split()]
        history = [line]
        while not all(x == 0 for x in history[-1]):
            new = []
            for i in range(1, len(history[-1])):
                new.append(history[-1][i] - history[-1][(i - 1)])
            history.append(new)
        answer += sum([x[-1] for x in history])
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 2
    answer = 0
    for line in input.splitlines():
        line = [int(x) for x in line.split()]
        history = [line]
        while not all(x == 0 for x in history[-1]):
            new = []
            for i in range(1, len(history[-1])):
                new.append(history[-1][i] - history[-1][(i - 1)])
            history.append(new)
    
        pred_val = history[-1][-1]
        for i in reversed(range(1, len(history))):
            pred_val = (history[i-1][0] - pred_val)
            
        answer += pred_val

    if test_case:
        print(f'(TEST) Part 2: {answer}')
        submit_if_correct(solve_part_2, answer, TRUE_ANSWER, DAY, 2, YEAR)
    else:
        print(f'(REAL) Part 2: {answer}')
    return answer


part1 = open(f"ex_inputs/day{DAY}/1.txt", "r")
solve_part_1(part1.read(), test_case=True)
part2 = open(f"ex_inputs/day{DAY}/2.txt", "r")
solve_part_2(part2.read(), test_case=True)

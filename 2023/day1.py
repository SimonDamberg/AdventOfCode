import re
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 1 # CHANGE THIS
# ------------------ #

text_to_digit = {
        "one": "o1ne", 
        "two": "t2wo",
        "three": "t3hree",
        "four": "f4our",
        "five": "f5ive",
        "six": "s6ix",
        "seven": "s7even",
        "eight": "e8ight",
        "nine": "n9ine",
    }

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 142
    data = input.split("\n")
    part_1 = sum([int(chunk[0] + chunk[-1]) for chunk in [re.findall(r"\d", line) for line in data]])
    if test_case:
        print(f'(TEST) Part 1: {part_1}')
        submit_if_correct(solve_part_1, part_1, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {part_1}')
    return part_1


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 281
    data = input.split("\n")
    new_data = []
    for row in data:
        for key, value in text_to_digit.items():
            row = row.replace(key, value)
        new_data.append(row)
    part_2 = sum([int(chunk[0] + chunk[-1]) for chunk in [re.findall(r"\d", line) for line in new_data]])
    if test_case:
        print(f'(TEST) Part 2: {part_2}')
        submit_if_correct(solve_part_2, part_2, TRUE_ANSWER, DAY, 2, YEAR)
    else:
        print(f'(REAL) Part 2: {part_2}')
    return part_2

part1=open(f"ex_inputs/day{DAY}/1.txt","r")
solve_part_1(part1.read(), test_case=True)
part2=open(f"ex_inputs/day{DAY}/2.txt","r")
solve_part_2(part2.read(), test_case=True)
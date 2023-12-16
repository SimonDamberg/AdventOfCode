from collections import defaultdict
import re
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 15 # CHANGE THIS
# ------------------ #

def hash(seq):
    curr_val = 0
    for char in seq:
        curr_val += ord(char)
        curr_val *= 17
        curr_val %= 256
    return curr_val

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 1320
    answer = 0
    for step in input.split(","):
        answer += hash(step)

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 145
    boxes = defaultdict(list) # box_num: list of tuples (label, focal_length)
    for step in input.split(","):
        label = re.findall(r'[a-z]+', step)[0]
        box = hash(label)

        if '-' in step: # removing
            for lens in boxes[box]:
                if label == lens[0]:
                    boxes[box].remove(lens)
                    break

        else: # adding
            focal_length = re.findall(r'[0-9]+', step)[0]
            
            # Replace if already in box
            found_lens = False
            for i, lens in enumerate(boxes[box]):
                if label == lens[0]:
                    boxes[box][i] = (label, int(focal_length))
                    found_lens = True
                    break
            # Add at the end if not in box
            if not found_lens:
                boxes[box].append((label, int(focal_length)))

    answer = 0
    for box_num, box in boxes.items():
        for box_pos, lens in enumerate(box):
            answer += (box_num+1) * (box_pos+1) * lens[1]

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
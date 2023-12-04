import re
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 3 # CHANGE THIS
# ------------------ #

def parse_input(input, part2):
    input = input.splitlines()
    width = len(input[0])
    height = len(input)
    grid = [[0 for x in range(width)] for y in range(height)]
    for line, y in zip(input, range(height)):
        numbers = re.findall(r"\d+", line)
        for number in numbers:
            start = line.index(number)
            end = start + len(number)
            for x in range(start, end):
                grid[y][x] = int(number)
            # replace num with 0 to support multi occurence of same number
            line = line[:start] + '0' * (end - start) + line[end:]

        for x in range(width):
            if part2:
                if line[x] == '*':
                    grid[y][x] = -1
                elif not line[x].isdigit():
                    grid[y][x] = 0
            else:
                if not line[x].isdigit() and line[x] != '.':
                    grid[y][x] = -1 # set all symbols to -1
    return grid

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 4361
    grid = parse_input(input, False)
    answer = 0
    for y in range(len(grid)):
        x = 0
        while x < len(grid[y]):
            if grid[y][x] > 0: # this is a number position
                number_length = len(str(grid[y][x]))
                found_symbol = False
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        for new_x in range(x, x + number_length):
                            if found_symbol:
                                break
                            if 0 <= y + dy < len(grid) and 0 <= new_x + dx < len(grid[0]):
                                if grid[y + dy][new_x + dx] == -1:
                                    answer += grid[y][x]
                                    found_symbol = True
            else:
                number_length = 1
            x += number_length
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 467835
    grid = parse_input(input, True)
    answer = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == -1:
                # check if gear has exactly two numbers next to it
                numbers = []
                skip_coords = set()
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]) and (y+dy, x+dx, grid[y + dy][x + dx]) not in skip_coords:
                            if grid[y + dy][x + dx] > 0:
                                found_number = grid[y + dy][x + dx]
                                numbers.append(found_number)
                                for new_dx in range(len(str(found_number))):
                                    # wouldn't work if duplicate number in same row with 1 spacing between them
                                    skip_coords.add((y+dy, x + dx + new_dx, grid[y + dy][x + dx]))
                if len(numbers) == 2:
                    answer += numbers[0] * numbers[1]

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
from collections import defaultdict
from submit_if_correct import submit_if_correct
import re
YEAR = 2023 

# ------------------ #
DAY = 2 # CHANGE THIS
# ------------------ #

def parse_input(input):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # -> { id: 1, blue: 6, red: 4, green: 2}
    input = input.splitlines()
    games = []
    for line in input:
        game = defaultdict(int)
        game['id'] = re.search(r'Game (\d+):', line).group(1)

        line = line.split(': ')[1]
        for color in line.split('; '):
            color = color.split(', ')
            for c in color:
                game[c.split(' ')[1]] = max(int(c.split(' ')[0]), game[c.split(' ')[1]])
        games.append(game)
    return games

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    TRUE_ANSWER = 8
    games = parse_input(input)

    answer = 0
    for game in games:
        if game['red'] <= MAX_RED and game['green'] <= MAX_GREEN and game['blue'] <= MAX_BLUE:
            answer += int(game['id'])
            
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 2286
    games = parse_input(input)
    answer = 0
    for game in games:
        answer += game['red'] * game['green'] * game['blue']

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
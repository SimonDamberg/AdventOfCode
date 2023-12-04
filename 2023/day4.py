from collections import deque
import re
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 4 # CHANGE THIS
# ------------------ #

def parse_input(input):
    input = input.splitlines()
    cards = []
    for card in input:
        id = int(re.findall(r"\d+", card.split(":")[0])[0])
        winning_numbers = [int(x) for x in re.findall(r"\d+", card.split(": ")[1].split(' | ')[0])]
        card_numbers = [int(x) for x in re.findall(r"\d+", card.split(": ")[1].split(' | ')[1])]
        cards.append({
            'id': id,
            'winning_numbers': winning_numbers,
            'card_numbers': card_numbers
        })
    return cards

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 13
    cards = parse_input(input)
    answer = 0
    for card in cards:
        correct_answers = len(set(card['winning_numbers']).intersection(set(card['card_numbers'])))
        answer += 2 ** (correct_answers - 1) if correct_answers > 0 else 0

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 30
    answer = 0
    cards = parse_input(input)
    num_cards = [1] * len(cards)
    for card in cards:
        answer += 1
        correct_answers = len(set(card['winning_numbers']).intersection(set(card['card_numbers'])))
        for i in range(correct_answers):
            num_cards[card['id'] + i] += num_cards[card['id'] - 1]
    answer = sum(num_cards)    
    if test_case:
        print(f'(TEST) Part 2: {answer}')
        submit_if_correct(solve_part_2, answer, TRUE_ANSWER, DAY, 2, YEAR)
    else:
        print(f'(REAL) Part 2: {answer}')
    return answer

# part1=open(f"ex_inputs/day{DAY}/1.txt","r")
# solve_part_1(part1.read(), test_case=True)
part2=open(f"ex_inputs/day{DAY}/2.txt","r")
solve_part_2(part2.read(), test_case=True)
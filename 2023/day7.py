import functools
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 7 # CHANGE THIS
# ------------------ #

def parse_hand(hand, use_joker=False):
    new_hand = []
    for card in hand:
        if card == "A":
            new_hand.append(14)
        elif card == "K":
            new_hand.append(13)
        elif card == "Q":
            new_hand.append(12)
        elif card == "J":
            if not use_joker:
                new_hand.append(11)
            else:
                new_hand.append(1)
        elif card == "T":
            new_hand.append(10)
        else:
            new_hand.append(int(card))
    return new_hand

def compare_hands(hand1,hand2):
    hand1, hand2 = hand1[0], hand2[0] # get rid of bid
    for card1,card2 in zip(hand1,hand2):
        if card1 == card2:
            continue
        else:
            return 1 if card1 < card2 else -1
    return 0

def count_winnings(hand_types):
    answer = 0
    curr_rank = 1
    for hand in hand_types:
        hand.sort(key=functools.cmp_to_key(compare_hands), reverse=True)
        for _, bid in hand:
            answer += curr_rank * int(bid)
            curr_rank += 1
    return answer

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 6440
    answer = 0
    hand_types = [[] for _ in range(7)]

    for line in input.split("\n"):
        hand, bid = line.split(" ")
        hand = parse_hand(hand)

        diff_cards = set(hand)
        if len(diff_cards) == 1: # all matches, five of a kind
            hand_types[6].append((hand, bid))
        elif len(diff_cards) == 2: # 4 or full house
            found_four = False
            for card in diff_cards:
                if hand.count(card) == 4:
                    hand_types[5].append((hand, bid)) # four of a kind
                    found_four = True
                    break
            if not found_four:
                hand_types[4].append((hand, bid)) # full house
        elif len(diff_cards) == 3: # two pairs, or three of a kind
            found_three = False
            for card in diff_cards:
                if hand.count(card) == 3:
                    hand_types[3].append((hand, bid)) # three of a kind
                    found_three = True
                    break
            if not found_three:
                hand_types[2].append((hand, bid)) # two pairs
        elif len(diff_cards) == 4: # one pair
            hand_types[1].append((hand, bid))
        else: # high card
            hand_types[0].append((hand, bid))
            
    answer = count_winnings(hand_types)

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 5905
    answer = 0
    hand_types = [[] for _ in range(7)]

    for line in input.split("\n"):
        hand, bid = line.split(" ")
        hand = parse_hand(hand, use_joker=True)

        diff_cards = set(hand)
        num_jokers = hand.count(1)

        if len(diff_cards) == 1: # all matches, five of a kind
            hand_types[6].append((hand, bid))

        elif len(diff_cards) == 2: # 4 or full house
            if num_jokers in [1, 2, 3, 4]:
                hand_types[6].append((hand, bid)) # use jokers to make five of a kind
            else:
                found_four = False
                for card in diff_cards:
                    if hand.count(card) == 4:
                        hand_types[5].append((hand, bid)) # four of a kind
                        found_four = True
                        break
                if not found_four:
                    hand_types[4].append((hand, bid)) # full house

        elif len(diff_cards) == 3: # two pairs, or three of a kind
            if num_jokers == 3:
                hand_types[5].append((hand, bid)) # use jokers to make four of a kind
            else:
                found_three = False
                for card in diff_cards:
                    if hand.count(card) == 3:
                        if num_jokers == 1:
                            hand_types[5].append((hand, bid)) # use joker to make four of a kind
                        else:
                            hand_types[3].append((hand, bid)) # three of a kind
                        found_three = True
                        break
                if not found_three:
                    if num_jokers == 2:
                        hand_types[5].append((hand, bid)) # use jokers to make four of a kind
                    elif num_jokers == 1:
                        hand_types[4].append((hand, bid)) # use joker to make full house
                    else:
                        hand_types[2].append((hand, bid)) # two pairs
                    
        elif len(diff_cards) == 4: # one pair
            if num_jokers == 2:
                hand_types[3].append((hand, bid)) # use jokers to make three of a kind
            elif num_jokers == 1:
                hand_types[3].append((hand, bid)) # use joker to make three of a kind
            else:
                hand_types[1].append((hand, bid))

        else: # high card
            if num_jokers == 1:
                hand_types[1].append((hand, bid)) # use joker to make one pair
            else:
                hand_types[0].append((hand, bid))
        
    answer = count_winnings(hand_types)

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
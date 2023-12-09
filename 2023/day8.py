import math
import re
from submit_if_correct import submit_if_correct
YEAR = 2023

# ------------------ #
DAY = 8  # CHANGE THIS
# ------------------ #

def parse_nodes(network):
    nodes = {}
    for line in network.splitlines():
        node, next_nodes = line.split(" = ")
        next_nodes = re.search(r'(\w+, \w+)', next_nodes).groups()[0].split(", ")
        nodes[node] = {
            "L": next_nodes[0],
            "R": next_nodes[1]
        }
    return nodes

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 2
    answer = 0
    instructions, network = input.split("\n\n")
    nodes = parse_nodes(network)
    node = "AAA"
    instr_idx = 0
    while node != "ZZZ":
        instruction = instructions[instr_idx]
        node = nodes[node][instruction]
        instr_idx = (instr_idx + 1) % len(instructions)
        answer += 1
    
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 6
    instructions, network = input.split("\n\n")
    nodes = parse_nodes(network)
    start_nodes = [x for x in nodes.keys() if x[-1] == "A"]
    
    # length of all paths to Z
    steps_to_Z = []
    for node in start_nodes:
        instr_idx = 0
        steps = 0
        while node[-1] != "Z":
            instruction = instructions[instr_idx]
            node = nodes[node][instruction]
            instr_idx = (instr_idx + 1) % len(instructions)
            steps += 1
        steps_to_Z.append(steps)

    # answer is LCM of all paths to Z
    lcm = steps_to_Z[0]
    for i in steps_to_Z[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    answer = lcm

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

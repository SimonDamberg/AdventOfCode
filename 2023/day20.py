from collections import defaultdict, deque
import math
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 20 # CHANGE THIS
# ------------------ #

def parse_input(input):
    broadcaster = []
    ffs = {}
    conjs = {}
    for line in input.splitlines():
        type, values = line.split(" -> ")
        if line[0] == "b":
            # broadcaster
            broadcaster = [x.strip() for x in values.split(",")]
        elif line[0] == "%":
            # flipflop
            ffs[type.split("%")[1]] = {
                "state": False,
                "outputs": [x.strip() for x in values.split(",")]
            }
        elif line[0] == "&":
            # conjunction
            conjs[type.split("&")[1]] = {
                "recent": defaultdict(bool),
                "outputs": [x.strip() for x in values.split(",")]
            }

    # for each ff, set outputed conjs state to false
    for ff in ffs:
        for output in ffs[ff]["outputs"]:
            if output in conjs:
                conjs[output]["recent"][ff] = False

    return broadcaster, ffs, conjs

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 32000000
    broadcaster, ffs, conjs = parse_input(input)

    low = 0
    high = 0
    for n in range(1000): # 1000 button presses
        low += 1 # button press to broadcaster
        stack = deque([('low', 'broad', x) for x in broadcaster])
        while stack:
            sig_type, src, dest = stack.popleft()
            #print(f"{src} -{sig_type}-> {dest}")
            if sig_type == "low":
                low += 1
            else:
                high += 1

            if dest in ffs:
                # flipflop, only send new if input was low
                if sig_type == "low":
                    ffs[dest]["state"] = not ffs[dest]["state"]
                    for output in ffs[dest]["outputs"]:
                        if ffs[dest]["state"]:
                            stack.append(("high", dest, output))
                        else:
                            stack.append(("low", dest, output))

            elif dest in conjs:
                # conjunction
                if sig_type == "low":
                    conjs[dest]["recent"][src] = False
                else:
                    conjs[dest]["recent"][src] = True
                for output in conjs[dest]["outputs"]:
                    if all(conjs[dest]["recent"].values()):
                        stack.append(("low", dest, output))
                    else:
                        stack.append(("high", dest, output))

    answer = low * high
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 0
    broadcaster, ffs, conjs = parse_input(input)

    # count length of each cycle that outputs to the conjunction that outputs to rx
    # LCM of these cycles is the answer

    # find conj with output to rx
    for conj in conjs:
        if "rx" in conjs[conj]["outputs"]:
            conj_to_rx = conj
            break

    # find conj with output to conj_to_rx
    conj_output_cycles_to_find = []
    for conj in conjs:
        if conj_to_rx in conjs[conj]["outputs"]:
            conj_output_cycles_to_find.append(conj)

    print(f"conj_ouput_cycles_to_find: {conj_output_cycles_to_find}")
    cycles = {x: 0 for x in conj_output_cycles_to_find}
    presses = 0
    while(any([x == 0 for x in cycles.values()])):
        presses += 1
        stack = deque([('low', 'broad', x) for x in broadcaster])
        while stack:
            sig_type, src, dest = stack.popleft()
            
            if dest == conj_to_rx and sig_type == "high":
                cycles[src] = presses

            if dest in ffs:
                # flipflop, only send new if input was low
                if sig_type == "low":
                    ffs[dest]["state"] = not ffs[dest]["state"]
                    for output in ffs[dest]["outputs"]:
                        if ffs[dest]["state"]:
                            stack.append(("high", dest, output))
                        else:
                            stack.append(("low", dest, output))

            elif dest in conjs:
                # conjunction
                if sig_type == "low":
                    conjs[dest]["recent"][src] = False
                else:
                    conjs[dest]["recent"][src] = True
                for output in conjs[dest]["outputs"]:
                    if all(conjs[dest]["recent"].values()):
                        stack.append(("low", dest, output))
                    else:
                        stack.append(("high", dest, output))
    
    # lcm of cycle lengths
    answer = math.lcm(*cycles.values())
    print(f'(REAL) Part 2 (not autosubmitted): {answer}')

part1=open(f"ex_inputs/day{DAY}/1.txt","r")
solve_part_1(part1.read(), test_case=True)
part2=open(f"ex_inputs/day{DAY}/2.txt","r")
solve_part_2(part2.read(), test_case=False)
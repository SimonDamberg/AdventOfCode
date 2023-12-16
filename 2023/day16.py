from collections import deque
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 16 # CHANGE THIS
# ------------------ 

dir_to_delta = {
    "r": (1, 0),
    "l": (-1, 0),
    "u": (0, -1),
    "d": (0, 1)
}

dir_to_arrow = {
    "r": ">",
    "l": "<",
    "u": "^",
    "d": "v"
}

def get_next_beams(beam, new_space, new_coords):
    next_beams = []
    match new_space:
        case ".":
            # continue forward
            next_beams.append((new_coords[0], new_coords[1], beam[2]))
        case "/":
            # right -> up, left -> down, up -> right, down -> left
            if beam[2] == "r":
                new_dir = "u"
            elif beam[2] == "l":
                new_dir = "d"
            elif beam[2] == "u":
                new_dir = "r"
            else:
                new_dir = "l"
            next_beams.append((new_coords[0], new_coords[1], new_dir))
        case "\\": # escape char
            # right -> down, left -> up, up -> left, down -> right
            if beam[2] == "r":
                new_dir = "d"
            elif beam[2] == "l":
                new_dir = "u"
            elif beam[2] == "u":
                new_dir = "l"
            else:
                new_dir = "r"
            next_beams.append((new_coords[0], new_coords[1], new_dir))
        case "|":
            # right, left -> split. up, down -> continue
            if beam[2] in "rl":
                next_beams.append((new_coords[0], new_coords[1], "u"))
                next_beams.append((new_coords[0], new_coords[1], "d"))
            else:
                next_beams.append((new_coords[0], new_coords[1], beam[2])) # continue
        case "-":
            # up, down -> split. right, left -> continue
            if beam[2] in "ud":
                next_beams.append((new_coords[0], new_coords[1], "l"))
                next_beams.append((new_coords[0], new_coords[1], "r"))
            else:
                next_beams.append((new_coords[0], new_coords[1], beam[2]))
    return next_beams

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 46
    grid = []
    for line in input.splitlines():
        row = []
        for space in line:
            row.append(space)
        grid.append(row)

    beams = deque([(-1, 0, "r")])
    energised = set()
    seen = set()
    while beams: 
        # get next beam
        beam = beams.popleft()

        # check if a beam has been here before in the same direction
        if beam in seen:
            continue
        else:
            seen.add(beam)
        delta = dir_to_delta[beam[2]]
        new_coords = (beam[0] + delta[0], beam[1] + delta[1])
        if 0 <= new_coords[0] < len(grid[0]) and 0 <= new_coords[1] < len(grid):
            energised.add(new_coords) # energise the new space
            new_space = grid[new_coords[1]][new_coords[0]]
            for next_beam in get_next_beams(beam, new_space, new_coords):
                beams.append(next_beam)

    answer = len(energised)
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer

def get_possible_start_positions(grid):
    # any edge on the top or bottom
    start_positions = []
    for x in range(len(grid[0])):
        start_positions.append((x, -1, "d"))
        start_positions.append((x, len(grid), "u"))
    # any edge on the left or right
    for y in range(len(grid)):
        start_positions.append((-1, y, "r"))
        start_positions.append((len(grid[0]), y, "l"))
    return start_positions
    
def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 51

    grid = []
    for line in input.splitlines():
        row = []
        for space in line:
            row.append(space)
        grid.append(row)

    answer = 0
    for start_pos in get_possible_start_positions(grid):
        beams = deque([start_pos])
        energised = set()
        seen = set()
        while beams: 
            # get next beam
            beam = beams.popleft()

            # check if a beam has been here before in the same direction
            if beam in seen:
                continue
            else:
                seen.add(beam)
            delta = dir_to_delta[beam[2]]
            new_coords = (beam[0] + delta[0], beam[1] + delta[1])
            if 0 <= new_coords[0] < len(grid[0]) and 0 <= new_coords[1] < len(grid):
                energised.add(new_coords) # energise the new space
                new_space = grid[new_coords[1]][new_coords[0]]
                for next_beam in get_next_beams(beam, new_space, new_coords):
                    beams.append(next_beam)
        answer = max(answer, len(energised))

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
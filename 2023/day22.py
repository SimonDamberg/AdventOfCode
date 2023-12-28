from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 22 # CHANGE THIS
# ------------------ #

def boxes_intersect_3d(box1, box2):
    x1a, y1a, z1a, x2a, y2a, z2a = box1
    x1b, y1b, z1b, x2b, y2b, z2b = box2

    # Check for x-axis overlap
    x_overlap = (x1a <= x2b and x2a >= x1b) or (x1b <= x2a and x2b >= x1a)

    # Check for y-axis overlap
    y_overlap = (y1a <= y2b and y2a >= y1b) or (y1b <= y2a and y2b >= y1a)

    # Check for z-axis overlap
    z_overlap = (z1a <= z2b and z2a >= z1b) or (z1b <= z2a and z2b >= z1a)

    return x_overlap and y_overlap and z_overlap

def is_supported(block_set, x,y,z):
    if z == 0:
        return True
    return (x,y,z) in block_set

def drop_bricks(bricks):
    # drops all possible bricks
    dropped = False

    block_set = set()
    for (x1,y1,z1,x2,y2,z2) in bricks:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                block_set.add((x,y,z2))

    new_bricks = []
    for brick in bricks:
        (x1, y1, z1, x2, y2, z2) = brick
        supported = False
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if is_supported(block_set, x, y, z1-1):
                    supported = True
                    break
            if supported:
                break
        if not supported:
            new_bricks.append((x1, y1, z1-1, x2, y2, z2-1))
            dropped = True
        else:
            new_bricks.append(brick)
    return dropped, new_bricks

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 5

    parsed_bricks = []
    for brick in input.splitlines():
        # split ~ and then split , to get the ends
        ends = brick.split("~")
        parsed_ends = []
        for end in ends:
            for coord in end.split(","):
                parsed_ends.append(int(coord))
        parsed_bricks.append(tuple(parsed_ends))    

    dropped = True
    while dropped:
        dropped, parsed_bricks = drop_bricks(parsed_bricks)

    # Check all bricks and see if anything moves when deleted
    answer = 0
    for i in range(len(parsed_bricks)):
        # delete current brick, if nothing moves, add 1 to answer
        bricks_copy = parsed_bricks.copy()
        del bricks_copy[i]
        fell, _ = drop_bricks(bricks_copy)
        if not fell:
            answer += 1

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 7

    parsed_bricks = []
    for brick in input.splitlines():
        # split ~ and then split , to get the ends
        ends = brick.split("~")
        parsed_ends = []
        for end in ends:
            for coord in end.split(","):
                parsed_ends.append(int(coord))
        parsed_bricks.append(tuple(parsed_ends))    

    dropped = True
    while dropped:
        dropped, parsed_bricks = drop_bricks(parsed_bricks)

    answer = 0
    for i in range(len(parsed_bricks)):
        bricks_copy = parsed_bricks.copy()
        del bricks_copy[i] # delete brick
        
        # dropped all bricks until nothing moves
        bricks_copy2 = bricks_copy.copy()
        dropped = True
        while dropped:
            dropped, bricks_copy2 = drop_bricks(bricks_copy2)

        # count how many bricks changes position
        changed = 0
        for (a, b) in zip(bricks_copy, bricks_copy2):
            if a != b:
                changed += 1
        answer += changed

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
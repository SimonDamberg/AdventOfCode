from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 13 # CHANGE THIS
# ------------------ #

def find_reflection_row(grid, allowed_non_matches=0):
    # try to reflect [0..i] to [i+1..len(grid)-1] and check if it matches
    for i in range(len(grid)-1):
        non_matching_places = 0
        for j in range(len(grid)):
            # check if row exists and if it matches
            if i+1+(i-j) in range(len(grid)) and grid[j] != grid[i+1+(i-j)]:
                non_matching_places += len([k for k in range(len(grid[j])) if grid[j][k] != grid[i+1+(i-j)][k]])
        if non_matching_places == allowed_non_matches:
            return i 
    return None

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 405
    answer = 0
    for num, pattern in enumerate(input.split("\n\n")):
        grid = [list(line) for line in pattern.split("\n")]
            
        # horizontal
        reflection_row = find_reflection_row(grid)
        if reflection_row is not None:
            answer += 100 * (reflection_row+1)
        else:  
            # vertical (check horizontal on transposed grid)
            transposed = [list(row) for row in zip(*grid)]
            reflection_col = find_reflection_row(transposed)
            if reflection_col is not None:
                answer += (reflection_col+1)
    
    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 400
    answer = 0
    for num, pattern in enumerate(input.split("\n\n")):
        grid = [list(line) for line in pattern.split("\n")]
            
        # horizontal
        reflection_row = find_reflection_row(grid, 2)
        if reflection_row is not None:
            answer += 100 * (reflection_row+1)
        else:  
            # vertical (check horizontal on transposed grid)
            transposed = [list(row) for row in zip(*grid)]
            reflection_col = find_reflection_row(transposed, 2)
            if reflection_col is not None:
                answer += (reflection_col+1)
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
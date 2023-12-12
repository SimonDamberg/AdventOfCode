import functools
from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 12 # CHANGE THIS
# ------------------ #


# dynamic programming
# spring_idx: current index within springs
# pattern_idx: current index within pattern
# curr_broken_length: current length of broken segment
DP = {}
def dp_replace_unknown(springs, pattern, spring_idx, pattern_idx, curr_broken_length):
    dp_key = (spring_idx, pattern_idx, curr_broken_length)
    
    # Return cached value if it exists
    if dp_key in DP:
        return DP[dp_key]
    
    # Base case: we've reached the end of springs
    if spring_idx == len(springs):
        if pattern_idx == len(pattern) and curr_broken_length == 0: # if we end on a working segment
            return 1
        elif pattern_idx == len(pattern)-1 and pattern[pattern_idx] == curr_broken_length: # if we end on a broken segment
            return 1
        else:
            return 0
    
    # Recursive case: replace ? with . and #, and recurse
    answer = 0
    for new_spring in [".", "#"]:
        if springs[spring_idx] == new_spring or springs[spring_idx] == "?": # this is same char or a ?, we continue recursing
            
            if new_spring == "." and curr_broken_length == 0: # in working segment, only increment spring_idx and continue
                answer += dp_replace_unknown(springs, pattern, spring_idx+1, pattern_idx, 0) 
            
            elif new_spring == "." and curr_broken_length > 0: # we have reached end of broken segment, reset count and move to next segment
                if pattern_idx < len(pattern) and pattern[pattern_idx] == curr_broken_length: # check if current broken segment matches pattern
                    answer += dp_replace_unknown(springs, pattern, spring_idx+1, pattern_idx+1, 0) # increment both spring_idx and pattern_idx, reset curr_broken_length
            
            elif new_spring == "#": # in broken segment, increment curr_broken_length and spring_idx
                answer += dp_replace_unknown(springs, pattern, spring_idx+1, pattern_idx, curr_broken_length+1) 

    DP[dp_key] = answer
    return answer            

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 21
    answer = 0
    for line in input.splitlines():
        springs, pattern = line.split(" ")
        pattern = [int(x) for x in pattern.split(",")]
        DP.clear() # important to clear cache between runs :))))))
        answer += dp_replace_unknown(springs, pattern, 0, 0, 0)

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 525152
    answer = 0
    #import tracemalloc
    #tracemalloc.start()
    for line in input.splitlines():
        springs, pattern = line.split(" ")
        springs = "?".join([springs, springs, springs, springs, springs])
        pattern = ",".join([pattern, pattern, pattern, pattern, pattern])
        pattern = [int(x) for x in pattern.split(",")]
        DP.clear() # important to clear cache between runs :))))))
        answer += dp_replace_unknown(springs, pattern, 0, 0, 0)

    #curr, peak = tracemalloc.get_traced_memory()
    #print(f"Peak memory usage was {round(peak / (1024*1024), 4)}MB")
    #tracemalloc.stop()
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
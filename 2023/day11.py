from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 11 # CHANGE THIS
# ------------------ #

def expand_universe(input, expand_num):
    rows = input.splitlines()
    galaxies = []
    new_galaxies = []
    for y, line in enumerate(rows):
        for x, space in enumerate(line):
            if space == "#":
                galaxies.append((x,y))
                new_galaxies.append((x,y))

    # expand row-wise
    for y, line in enumerate(rows):
        if all(space == "." for space in line):
            for i, galaxy in enumerate(galaxies):
                if galaxy[1] > y:
                    new_galaxies[i] = (new_galaxies[i][0], new_galaxies[i][1] + expand_num)

    # expand column-wise
    for x in range(len(rows[0])):
        if all(line[x] == "." for line in rows):
            for i, galaxy in enumerate(galaxies):
                if galaxy[0] > x:
                    new_galaxies[i] = (new_galaxies[i][0] + expand_num, new_galaxies[i][1])
    
    return new_galaxies

def count_neighbor_lengths(galaxies):
    sum = 0
    for i, galaxy in enumerate(galaxies):
        for other_galaxy in galaxies[i+1:]:
            if galaxy != other_galaxy:
                dx = abs(galaxy[0] - other_galaxy[0])
                dy = abs(galaxy[1] - other_galaxy[1])
                sum += dx + dy
    return sum

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 374
    new_galaxies = expand_universe(input, 1)
    answer = count_neighbor_lengths(new_galaxies)

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 82000210
    new_galaxies = expand_universe(input, 1000000 - 1)
    answer = count_neighbor_lengths(new_galaxies)
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
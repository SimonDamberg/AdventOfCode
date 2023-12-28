import itertools
from submit_if_correct import submit_if_correct
YEAR = 2023 
from shapely.geometry import LineString

# ------------------ #
DAY = 24 # CHANGE THIS
# ------------------ #


def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    hailstones = []
    for line in input.splitlines():
        pos, vel = line.split(' @ ')
        pos = tuple([int(x.strip()) for x in pos.split(',')])
        vel = tuple([int(x.strip()) for x in vel.split(',')])
        hailstones.append((pos, vel))
    
    MIN = 200000000000000
    MAX = 400000000000000 
    answer = 0
    for stone1, stone2 in itertools.combinations(hailstones, 2):
        # IGNORE Z-axis for now :^)
        (start_x1, start_y1, _), (vx1, vy1, _) = stone1
        (start_x2, start_y2, _), (vx2, vy2, _) = stone2
        
        # Algebra to check intersection point of two lines
        # y = kx + m
        k1 = vy1 / vx1
        k2 = vy2 / vx2

        # If the lines are parallel, they will never intersect
        if k1 == k2:
            continue

        m1 = start_y1 - k1 * start_x1
        m2 = start_y2 - k2 * start_x2

        # Intersection point
        x = (m2 - m1) / (k1 - k2)
        y = k1 * x + m1

        # check if the intersection point is on the line segment
        if (x < start_x1 and vx1 > 0) or (x > start_x1 and vx1 < 0) or (x < start_x2 and vx2 > 0) or (x > start_x2 and vx2 < 0):
            continue

        # Check if the intersection point is within MAX and MIN
        if MIN <= x <= MAX and MIN <= y <= MAX:
            answer += 1

    print(f'(REAL) Part 1 (Not submitted): {answer}')
    return answer


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    hailstones = []
    for line in input.splitlines():
        pos, vel = line.split(' @ ')
        pos = tuple([int(x.strip()) for x in pos.split(',')])
        vel = tuple([int(x.strip()) for x in vel.split(',')])
        hailstones.append((pos, vel))
    
    # Use z3 to solve the system of equations
    # Feels like cheating but can't figure out a general solution :(

    import z3

    # Create the variables
    start_x = z3.Int('start_x')
    start_y = z3.Int('start_y')
    start_z = z3.Int('start_z')
    vel_x = z3.Int('vel_x')
    vel_y = z3.Int('vel_y')
    vel_z = z3.Int('vel_z')

    # Create the solver
    solver = z3.Solver()
    # Iterate through stones and add the constraints
    for idx, stone in enumerate(hailstones):
        # Unpack stone
        (x, y, z), (vx, vy, vz) = stone

        # Time variable for this stone
        time = z3.Int(f'time_{idx}')

        # Add the constraints for collision with our stone and the current stone
        solver.add(time >= 0)
        solver.add(start_x + vel_x * time == x + vx * time)
        solver.add(start_y + vel_y * time == y + vy * time)
        solver.add(start_z + vel_z * time == z + vz * time)

    assert solver.check() == z3.sat # Check if the constraints are satisfiable
    model = solver.model()
    answer = model.eval(start_x + start_y + start_z)
    print(f'(REAL) Part 2 (Not submitted): {answer}')

part1=open(f"ex_inputs/day{DAY}/1.txt","r")
solve_part_1(part1.read(), test_case=True)
part2=open(f"ex_inputs/day{DAY}/2.txt","r")
solve_part_2(part2.read(), test_case=True)
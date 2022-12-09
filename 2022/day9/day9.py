from math import copysign 

dir_to_pos = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

def simulate(num_knots, lines):
    visited = set()
    rope = [(0.0, 0.0) for _ in range(num_knots + 1)] # Also add the head
    for line in lines:
        line = line.split(" ")
        dir = dir_to_pos[line[0]]
        steps = int(line[1])
        for _ in range(steps):
            # Move head
            rope[0] = (rope[0][0] + dir[0], rope[0][1] + dir[1])
            
            # Go through each knot and move if necessary
            for i in range(1, len(rope)):
                knot_x_diff = rope[i-1][0] - rope[i][0]
                knot_y_diff = rope[i-1][1] - rope[i][1]
                # Check if knot is more than 1 step away from head in any direction
                if abs(knot_x_diff) > 1 and abs(knot_y_diff) > 0 or abs(knot_y_diff) > 1 and abs(knot_x_diff) > 0:
                    # Move diagonally 1 step towards head
                    rope[i] = (rope[i][0] + copysign(1, knot_x_diff), rope[i][1] + copysign(1, knot_y_diff))
                elif abs(knot_x_diff) > 1:
                    # Move horizontally 1 step towards head
                    rope[i] = (rope[i][0] + copysign(1, knot_x_diff), rope[i][1])
                elif abs(knot_y_diff) > 1:
                    # Move vertically 1 step towards head
                    rope[i] = (rope[i][0], rope[i][1] + copysign(1, knot_y_diff))
            
            # Add current location of last knot to visited
            visited.add(rope[-1])
    return len(visited)

print(f"Part 1: {simulate(1, lines)}")
print(f"Part 2: {simulate(9, lines)}")


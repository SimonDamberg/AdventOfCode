largest_y = 0
blocked_pos = set()
with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        coords = line.split(" -> ")
        coords = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in coords]
        # sorry for bad parsing :(
        for i in range(len(coords)-1):
            curr = coords[i]
            next = coords[i + 1]

            # Save largest y
            largest_y = max(largest_y, curr[1])

            if curr[0] == next[0]:
                if curr[1] < next[1]:
                    # down
                    for y in range(curr[1], next[1]+1):
                        blocked_pos.add((curr[0], y))
                else:
                    # up
                    for y in range(next[1], curr[1]+1):
                        blocked_pos.add((curr[0], y))
            else:
                if curr[0] < next[0]:
                    # right
                    for x in range(curr[0], next[0]+1):
                        blocked_pos.add((x, curr[1]))
                else:
                    # left
                    for x in range(next[0], curr[0]+1):
                        blocked_pos.add((x, curr[1]))

curr_sand = (500, 0)
resting_sand = 0
pt_1_done = False
while curr_sand not in blocked_pos:
    
    if not pt_1_done and curr_sand[1] > largest_y:
        pt_1_done = True
        print(f"Part 1: {resting_sand}")

    elif curr_sand[1] > largest_y:
            # Add to blocked_pos and spawn new sand
            blocked_pos.add(curr_sand)
            curr_sand = (500, 0)
            resting_sand += 1
    # Try to move down
    elif (curr_sand[0], curr_sand[1] + 1) not in blocked_pos:
        curr_sand = (curr_sand[0], curr_sand[1] + 1)
    # Try to move diagonally to left
    elif (curr_sand[0] - 1, curr_sand[1] + 1) not in blocked_pos:
        curr_sand = (curr_sand[0] - 1, curr_sand[1] + 1)
    # Try to move diagonally to right
    elif (curr_sand[0] + 1, curr_sand[1] + 1) not in blocked_pos:
        curr_sand = (curr_sand[0] + 1, curr_sand[1] + 1)
    else:
        # Add to blocked_pos and spawn new sand
        blocked_pos.add(curr_sand)
        curr_sand = (500, 0)
        resting_sand += 1

print(f"Part 2: {resting_sand}")
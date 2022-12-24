from collections import deque
import numpy as np
dir_coords = {"<":(-1, 0),
     ">":(1,0),
     "v":(0,1),
     "^":(0,-1)}

with open("input.txt") as f:
    lines = f.read().splitlines()
    max_x = len(lines[0])-2
    max_y = len(lines)-2
    start = (lines[0].index("."), 0)
    end = (lines[-1].index("."), len(lines)-1)
    blizzards = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in ["<", ">", "^", "v"]:
                blizzards.append([x, y, dir_coords[c]])

def update_blizzards():
    for blizz in blizzards:
        x, y, (dx, dy) = blizz
        blizz[0] = ((x + dx - 1) % max_x) + 1 # Should never reach border
        blizz[1] = ((y + dy - 1) % max_y) + 1 # Should never reach border

visited = set()
blocked = set()
queue = deque([(start, 0, False, False)])
max_minutes_reached = -1
pt_1_done = False
while queue:
    node, curr_minute, reached_end, reached_start = queue.popleft()
    x, y = node

    if node == end and reached_start and reached_end:
        print(f"Part 2: {curr_minute}") # 942
        break

    if curr_minute > max_minutes_reached:
        # Only update blizzards if we have moved further than before
        max_minutes_reached = curr_minute
        update_blizzards()
        blocked = set()
        for blizz in blizzards:
            blocked.add((blizz[0], blizz[1]))

    if (node, curr_minute, reached_end, reached_start) in visited:
        continue
    else:
        visited.add((node, curr_minute, reached_end, reached_start))

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
        new_x = x + dx
        new_y = y + dy
        # Check if new pos is blocked by blizzard and not out of bounds, or if it is start or end
        if (new_x, new_y) not in blocked and new_x in range(1, max_x+1) and new_y in range(1, max_y+1) or \
            (new_x, new_y) == start or (new_x, new_y) == end:
            
            # At end, print part 1 if first time and set reached_end to True
            if (new_x, new_y) == end:
                if not pt_1_done:
                    pt_1_done = True
                    print(f"Part 1: {curr_minute+1}") # 332
                queue.append(((new_x, new_y), curr_minute+1, True, reached_start))

            # If we have gotten to end and then returned back to start
            elif (new_x, new_y) == start and reached_end:
                queue.append(((new_x, new_y), curr_minute+1, reached_end, True))

            # All other tiles
            else:
                queue.append(((new_x, new_y), curr_minute+1, reached_end, reached_start))
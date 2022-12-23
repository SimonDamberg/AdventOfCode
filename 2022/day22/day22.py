
def parse_input(file):
    opened = set()
    blocked = set()
    max_x = 0
    max_y = 0
    pos = None
    with open(file, "r") as f:
        map, seq = f.read().split("\n\n")
        seq = seq.replace("R", " R ").replace("L", " L ").replace(" ", " ").split(" ")
        for y, line in enumerate(map.split("\n")):
            max_y = max(max_y, y+1)
            for x, c in enumerate(line):
                max_x = max(max_x, x+1)
                if c == "#":
                    blocked.add((x+1,y+1))
                elif c == ".":
                    opened.add((x+1,y+1))
                    if y == 0 and pos is None:
                        pos = (x+1, y+1)
    return pos, seq, opened, blocked, max_x, max_y
    
def get_cube_side(x, y):
    if y <= 50 and 50<x<=100:
        return 1
    elif y <= 50 and x > 100:
        return 2
    elif 50<y<=100 and 50<x<=100:
        return 3
    elif 100<y<=150 and x<=50:
        return 4
    elif 100<y<=150 and 50<x<=100:
        return 5
    elif y>150 and x<=50:
        return 6
    else:
        return -1

def part1_wrapping(facing, new_x, new_y, blocked, opened):
    found_wall = False
    pos = None
    if facing == 0:
        # new_x should be smallest possible value in either walled or opened with same y
        for n in range(1, new_x):
            if (n, new_y) in blocked:
                found_wall = True
                break
            elif (n, new_y) in opened:
                pos = (n, new_y)
                break
    elif facing == 1:
        # new_y should be smallest possible y in same x
        for n in range(1, new_y):
            if (new_x, n) in blocked:
                found_wall = True
                break
            elif (new_x, n) in opened:
                pos = (new_x, n)
                break
    elif facing == 2:
        # new_x shoudl be largest possible x in same y
        for n in range(max_x, new_x, -1):
            if (n, new_y) in blocked:
                found_wall = True
                break
            elif (n, new_y) in opened:
                pos = (n, new_y)
                break
    else:
        # new_y should be largest possible y in same x
        for n in range(max_y, new_y, -1):
            if (new_x, n) in blocked:
                found_wall = True
                break
            elif (new_x, n) in opened:
                pos = (new_x, n)
                break
    return found_wall, pos

def part2_wrapping(facing, x, y):
    """
    To understand wrapping rules, see mapping.png
    """
    from_cube = get_cube_side(x, y)
    new_facing = facing
    new_x = x
    new_y = y
    if from_cube == 1:
        if facing == 2: # 1 -> 4, wrapping
            # L facing becomes R
            new_facing = 0
            new_x = 1
            # y=1 => y=150, y=50 => y=101
            # WEIRD
            new_y = 151-y
        elif facing == 3: # 1 -> 6, wrapping
            # U facing becomes R
            new_facing = 0
            new_x = 1
            # x=51 => y=151, x=100 => y=200
            new_y = x+100
    elif from_cube == 2:
        if facing == 0: # 2 -> 5, wrapping
            # R facing becomes L
            new_facing = 2
            new_x = 100
            # y = 1 => y=150, y=50 => y=101
            new_y = 151-y
        elif facing == 3: # 2 -> 6, wrapping
            # unchanged facing
            new_facing = 3
            new_x = x - 100
            new_y = 200
        elif facing == 1: # 2 -> 3, wrapping
            # D facing vecomes L 
            new_facing = 2
            new_x = 100
            new_y = x-50
    elif from_cube == 3:
        if facing == 2: # 3 -> 4, wrapping
            # L facing becomes D
            new_facing = 1
            # y = 51 => x = 1, y = 100 => x = 50
            new_x = y - 50
            new_y = 101
        elif facing == 0: # 3 -> 2, wrapping
            # R facing becomes U
            new_facing = 3
            # y = 51 => x = 101, y = 100 => x = 150
            new_x = y + 50
            new_y = 50
    elif from_cube == 4:
        if facing == 2: # 4 -> 1, wrapping
            # L facing becomes R
            new_facing = 0
            new_x = 51
            # y=101 => y=50, y=150 => y=1
            new_y = 151-y
        elif facing == 3: # 4 -> 3, wrapping
            # U facing becomes R
            new_facing = 0
            new_x = 51
            # x = 1 => y = 51, x = 50 => y = 100
            new_y = x + 50
    elif from_cube == 5:
        if facing == 0: # 5 -> 2, wrapping
            # R facing becomes L
            new_facing = 2
            new_x = 150
            # y=101 => y=50, y=150 => y=1
            new_y = 151-y
        elif facing == 1: # 5 -> 6, wrapping
            # D facing becomes L 
            new_facing = 2
            new_x = 50
            # x = 51 => y=151, x = 100 => y=200
            new_y = x + 100
    elif from_cube == 6:
        if facing == 0: # 6 -> 5, wrapping
            # R facing becomes U
            new_facing = 3
            # 151=>51, 200=>100
            new_x = y-100
            new_y = 150
        elif facing == 1: # 6 -> 2, wrapping
            # unchanged facing
            new_facing = 1
            new_y = 1
            # x=1 => x=101, x=50 => x=150
            new_x = x+100
        elif facing == 2: # 6 -> 1, wrapping
            # L facing becomes D
            new_facing = 1
            # y=151 => x=51, y=200 => x=100
            new_x = y-100
            new_y = 1 
    return (new_x, new_y), new_facing 

def solve(pos, facing, seq, opened, blocked, part1):
    for step in seq:
        if step.isdigit():
            steps = int(step)
            for i in range(steps):
                dx, dy = facing_to_dir[facing]
                new_x, new_y = pos[0]+dx, pos[1]+dy
                if (new_x, new_y) in blocked:
                    break
                elif (new_x, new_y) in opened:
                    pos = (new_x, new_y)
                else:
                    if part1:
                        found_wall, new_pos = part1_wrapping(facing, new_x, new_y, blocked, opened) 
                        if found_wall:
                            break
                        else:
                            pos = new_pos
                    else:
                        new_pos, new_facing = part2_wrapping(facing, pos[0], pos[1])                    
                        if new_pos in blocked:
                            break
                        else:
                            pos = new_pos
                            facing = new_facing
        else:
            if step == "R":
                facing = (facing + 1) % 4
            else:
                facing = (facing - 1) % 4
    return (4*pos[0]) + (1000*pos[1]) + facing

facing_to_dir = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1)
}

facing = 0 # 0 = right, 1 = down, 2 = left, 3 = up
pos, seq, opened, blocked, max_x, max_y = parse_input("input.txt")
print(f"Part 1: {solve(pos, facing, seq, opened, blocked, True)}") # 122082

pos, seq, opened, blocked, max_x, max_y = parse_input("input.txt")
facing = 0
print(f"Part 2: {solve(pos, facing, seq, opened, blocked, False)}") # 134076
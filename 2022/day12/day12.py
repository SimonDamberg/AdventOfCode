start_pos = (0, 0)
coords = {}
with open("input.txt", "r") as f:
    for i, line in enumerate(f.read().splitlines()):
        for j, c in enumerate(line):
            coords[(i, j)] = c
            if c == "E": # Start from end
                start_pos = (i, j)

def get_height(char):
    if char == "S":
        return ord("a")
    elif char == "E":
        return ord("z")
    else:
        return ord(char)

# Reverse BFS from end
for part, end in [("Part 1", "S"), ("Part 2", "a")]:
    q = [(start_pos, 0)]
    visited = set(start_pos)
    while q:
        pos, dist = q.pop(0)
        x, y = pos

        if coords[pos] == end:
            print(f"{part}: {dist}")
            break

        for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (new_x, new_y) in coords and (new_x, new_y) not in visited and get_height(coords[pos]) - get_height(coords[(new_x, new_y)]) <= 1:
                visited.add((new_x, new_y))
                q.append(((new_x, new_y), dist+1))
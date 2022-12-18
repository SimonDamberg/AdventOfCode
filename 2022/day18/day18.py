from collections import deque

cubes = set()
with open('input.txt', "r") as f:
    for line in f.read().splitlines():
        x, y, z = line.split(",")
        cubes.add((int(x), int(y), int(z)))

max_x = max([x for x, _, _ in cubes])
max_y = max([y for _, y, _ in cubes]) 
max_z = max([z for _, _, z in cubes])

surface_area_1 = 0
for cube in cubes:
    x, y, z = cube
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        if (x+dx, y+dy, z+dz) not in cubes:
            surface_area_1 += 1
print(f"Part 1: {surface_area_1}")

# BFS to "floodfill" the grid and count surfaces
air = set()
q = deque()
q.append((-1, -1, -1))
surface_area_2 = 0
while q:
    x, y, z = q.popleft()
    if (x, y, z) in air:
        continue
    air.add((x, y, z))
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        if -1 <= x+dx <= max_x+1 and -1 <= y+dy <= max_y+1 and -1 <= z+dz <= max_z+1:
            if (x+dx, y+dy, z+dz) not in cubes: 
                q.append((x+dx, y+dy, z+dz))
            else:
                surface_area_2 += 1

print(f"Part 2: {surface_area_2}")
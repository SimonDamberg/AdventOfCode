import heapq
import math

def djikstra(coords):
    last_x, last_y = max(coords)
    dest = (last_x, last_y)
    visited = set()
    q = [(0, (0, 0))]
    min_distance = {(0, 0): 0}
    
    while q:
        dist, node = heapq.heappop(q)
        
        if node == dest:
            # Done
            return dist
        
        if node in visited:
            # Already checked
            continue
            
        visited.add(node)
        x, y = node

        # Explore all neighbors
        for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            
            # Check if valid tile (edges etc)
            if last_x >= new_x >= 0 and last_y >= new_y >= 0:
                
                neigh = (new_x, new_y)
                if neigh in visited:
                    # Already checked
                    continue

                new_distance = dist + coords[(new_x, new_y)] # Calculate new distance when ENTERING
                if neigh in min_distance and new_distance < min_distance[neigh]:
                    min_distance[neigh] = new_distance
                    heapq.heappush(q, (new_distance, neigh))
                else:
                    min_distance[neigh] = new_distance
                    heapq.heappush(q, (new_distance, neigh))
    return math.inf # No path found

# Part 1: Regular coords
coords = {}
with open("input.txt", "r") as f:
    for i, line in enumerate(f.read().splitlines()):
        for j, c in enumerate(line):
            coords[(i, j)] = int(c)

print(f"Part 1: {djikstra(coords)}")

# Part 2: Modified coords
coords = {}
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    w, h = len(lines[0]), len(lines)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            # Each tile should be added 5 times in both directions, incremented by 1
            for y_aux in range(5):
                for x_aux in range(5):
                    new_val = int(c)+x_aux+y_aux
                    if new_val > 9:
                        new_val -= 9
                        
                    coords[(x_aux * w + x, y_aux * h + y)] = new_val

print(f"Part 2: {djikstra(coords)}")
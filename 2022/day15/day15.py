sensors = set()
beacons = set()
blocked_pos = set()
sens_to_manhattan_dist = dict()
smallest_x = 0
largest_x = 0

with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        sensor, beacon = line.split("beacon ")
        sen_x = int(sensor.split("x=")[1].split(",")[0])
        sen_y = int(sensor.split("y=")[1].split(":")[0])
        beac_x = int(beacon.split("x=")[1].split(",")[0])
        beac_y = int(beacon.split("y=")[1].split(":")[0])
        beacons.add((beac_x, beac_y))
        sensors.add((sen_x, sen_y))
        manhattan_dist = abs(sen_x - beac_x) + abs(sen_y - beac_y)

        smallest_x = min(smallest_x, sen_x-manhattan_dist)
        largest_x = max(largest_x, sen_x+manhattan_dist)
        sens_to_manhattan_dist[(sen_x, sen_y)] = manhattan_dist

searched_y = 2000000
blocked_in_row = set()
for x in range(smallest_x, largest_x + 1):
    for sensor, sensor_manhattan_dist in sens_to_manhattan_dist.items():
        if abs(x - sensor[0]) + abs(searched_y - sensor[1]) <= sensor_manhattan_dist:
            if (x, searched_y) not in sensors and (x, searched_y) not in beacons:
                blocked_in_row.add((x, searched_y))

print(f"Part 1: {len(blocked_in_row)}") 

# Part 2
# Since there is only one possible signal position
# It HAS to be distance+1 away from two sensors
for (x, y), d in sens_to_manhattan_dist.items():
    # Check all points d+1 away from (x,y)
    for dx in range(d+2):
        dy = (d+1)-dx
        for x_dir, y_dir in [(-1,-1),(-1,1),(1,-1),(1,1)]: # Check all 4 directions
            new_x = x + (x_dir*dx)
            new_y = y + (y_dir*dy)

            # check that coords are in bounds
            if 0 < new_x <= 4000000 and 0 < new_y <= 4000000:
                not_inside_other_sensor = True
                for (s2x, s2y), s2d in sens_to_manhattan_dist.items():
                    # Check if new_x, new_y is inside any other sensor
                    if abs(new_x - s2x) + abs(new_y - s2y) <= s2d:
                        not_inside_other_sensor = False
                        break
                if not_inside_other_sensor:
                    print(f"Part 2: {(new_x*4000000) + new_y}")
                    exit()

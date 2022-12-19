from functools import cache
import numpy as np 

class Blueprint:
    def __init__(self, id, input):
        self.id = id
        self.ore_cost = input[0]
        self.clay_cost = input[1]
        self.obsidian_cost = input[2:4] # first is ore, second is clay
        self.geode_cost = input[4:6] # first is ore, second is obsidian

        self.max_ore_cost = max(self.ore_cost, self.clay_cost, self.obsidian_cost[0], self.geode_cost[0])
        self.max_clay_cost = max(self.clay_cost, self.obsidian_cost[1])
        self.max_obsidian_cost = self.geode_cost[1]

    def __repr__(self):
        return f"\n====== Blueprint {self.id} ===== \n Ore: {self.ore_cost}\n Clay: {self.clay_cost}\n Obsidian{self.obsidian_cost}\n Geode{self.geode_cost}"

blueprints = {}
with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        # get all numbers in line
        id = int(line.split("Blueprint ")[1].split(":")[0])
        blueprints[Blueprint(id, [int(s) for s in line.split(" ") if s.isdigit()])] = 0

@cache
def sim(blueprint, time, robots, outputs, max_time):
    if time == max_time:
        return outputs[3]+robots[3]

    # Output gained this minute
    best = 0

    # Only add resources if they can be used up
    new_outputs = (outputs[0], outputs[1], outputs[2], outputs[3]+robots[3])
    if outputs[0] < (blueprint.max_ore_cost * (max_time-time)):
        new_outputs = (new_outputs[0] + robots[0], new_outputs[1], new_outputs[2], new_outputs[3])
    if outputs[1] < (blueprint.max_clay_cost * (max_time-time)):
        new_outputs = (new_outputs[0], new_outputs[1] + robots[1], new_outputs[2], new_outputs[3])
    if outputs[2] < (blueprint.max_obsidian_cost * (max_time-time)):
        new_outputs = (new_outputs[0], new_outputs[1], new_outputs[2] + robots[2], new_outputs[3])

    # Try to build ore robot if possible
    if outputs[0] >= blueprint.ore_cost and robots[0] < blueprint.max_ore_cost:
        out = (new_outputs[0] - blueprint.ore_cost, new_outputs[1], new_outputs[2], new_outputs[3])
        new_robots = (robots[0] + 1, robots[1], robots[2], robots[3])
        #print(f"Building ore robot at time {time} with {outputs} -> {new_outputs}, {robots} -> {new_robots}")
        best = max(best, sim(blueprint, time + 1, new_robots, out, max_time))
    
    # Try to build clay robot if possible
    if outputs[0] >= blueprint.clay_cost and robots[1] < blueprint.max_clay_cost:
        out = (new_outputs[0] - blueprint.clay_cost, new_outputs[1], new_outputs[2], new_outputs[3])
        new_robots = (robots[0], robots[1] + 1, robots[2], robots[3])
        #print(f"Building clay robot at time {time} with {outputs} -> {new_outputs}, {robots} -> {new_robots}")
        best = max(best, sim(blueprint, time + 1, new_robots, out, max_time))
    
    # Try to build obsidian robot if possible
    if outputs[0] >= blueprint.obsidian_cost[0] and outputs[1] >= blueprint.obsidian_cost[1] and robots[2] < blueprint.max_obsidian_cost:
        out = (new_outputs[0] - blueprint.obsidian_cost[0], new_outputs[1] - blueprint.obsidian_cost[1], new_outputs[2], new_outputs[3])
        new_robots = (robots[0], robots[1], robots[2] + 1, robots[3])
        best = max(best, sim(blueprint, time + 1, new_robots, out, max_time))
    
    # Try to build geode robot if possible
    if outputs[0] >= blueprint.geode_cost[0] and outputs[2] >= blueprint.geode_cost[1]:
        out = (new_outputs[0] - blueprint.geode_cost[0], new_outputs[1], new_outputs[2] - blueprint.geode_cost[1], new_outputs[3])
        new_robots = (robots[0], robots[1], robots[2], robots[3] + 1)
        best = max(best, sim(blueprint, time + 1, new_robots, out, max_time))

    best = max(best, sim(blueprint, time + 1, robots, new_outputs, max_time))
    return best

total_quality = 0
for bp in blueprints.keys():
    sim.cache_clear()
    geodes = sim(bp, 1, (1, 0, 0, 0), (0, 0, 0, 0), 24)
    print(f"Blueprint {bp.id} can make {geodes} geodes in 24 minutes with total quality of {geodes * bp.id}")
    total_quality += geodes * bp.id

print(f"Part 1: {total_quality}")

# pt_2_geodes = 1
# for bp in blueprints.keys():
#     if bp.id > 3:
#         continue
#     sim.cache_clear()
#     geodes = sim(bp, 1, (1, 0, 0, 0), (0, 0, 0, 0), 32)
#     print(f"Blueprint {bp.id} can make {geodes} geodes in 32 minutes")
#     pt_2_geodes *= geodes

# print(f"Part 2: {pt_2_geodes}")
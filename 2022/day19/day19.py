from functools import cache
import numpy as np 

blueprints = []
with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        # get all numbers in line
        id = int(line.split("Blueprint ")[1].split(":")[0])
        blueprints.append([int(s) for s in line.split(" ") if s.isdigit()])

@cache
def sim(time, ore_robots, c_robots, obs_robots, geo_robots, ore, clay, obsidian):
    if time == max_time:
        return geo_robots

    # Only add resources if they can be used up
    if ore < (max_ore_cost * (max_time-time)):
        capped_ore = ore_robots + ore
    else:
        capped_ore = ore
    if clay < (max_clay_cost * (max_time-time)):
        capped_clay = c_robots + clay
    else:
        capped_clay = clay
    if obsidian < (max_obsidian_cost * (max_time-time)):
        capped_obsidian = obs_robots + obsidian
    else:
        capped_obsidian = obsidian

    best = 0

    # Try to build ore robot if possible
    if ore >= bp[0] and ore_robots < max_ore_cost:
        best = max(best, sim(time+1, ore_robots + 1, c_robots, obs_robots, geo_robots, capped_ore - bp[0], capped_clay, capped_obsidian))
    
    # Try to build clay robot if possible
    if ore >= bp[1] and c_robots < max_clay_cost:
        best = max(best, sim(time+1, ore_robots, c_robots + 1, obs_robots, geo_robots, capped_ore - bp[1], capped_clay, capped_obsidian))
    
    # Try to build obsidian robot if possible
    if ore >= bp[2] and clay >= bp[3] and obs_robots < max_obsidian_cost:
        best = max(best, sim(time+1, ore_robots, c_robots, obs_robots + 1, geo_robots, capped_ore - bp[2], capped_clay - bp[3], capped_obsidian))
    
    # Try to build geode robot if possible
    if ore >= bp[4] and obsidian >= bp[5]:
        best = max(best, sim(time+1, ore_robots, c_robots, obs_robots, geo_robots + 1, capped_ore - bp[4], capped_clay, capped_obsidian - bp[5]))

    if ore_robots != max_ore_cost or c_robots != max_clay_cost or obs_robots != max_obsidian_cost:
        best = max(best, sim(time+1, ore_robots, c_robots, obs_robots, geo_robots, capped_ore, capped_clay, capped_obsidian))
    
    return geo_robots + best

total_quality = 0
max_time = 24
for n in range(len(blueprints)):
    bp = blueprints[n]
    max_ore_cost = max(bp[0], bp[1], bp[2], bp[4])
    max_clay_cost = max(bp[1], bp[3])
    max_obsidian_cost = bp[5]
    sim.cache_clear()
    geodes = sim(1, 1, 0, 0, 0, 0, 0, 0)
    print(f"Blueprint {n+1} can make {geodes} geodes in 24 minutes with total quality of {geodes * (n+1)}")
    total_quality += geodes * (n+1)
print(f"Part 1: {total_quality}")

pt_2_geodes = 1
max_time = 32
for n in range(0, 3):
    bp = blueprints[n]
    max_ore_cost = max(bp[0], bp[1], bp[2], bp[4])
    max_clay_cost = max(bp[1], bp[3])
    max_obsidian_cost = bp[5]
    sim.cache_clear()
    geodes = sim(1, 1, 0, 0, 0, 0, 0, 0)
    print(f"Blueprint {n+1} can make {geodes} geodes in 32 minutes")
    pt_2_geodes *= geodes
print(f"Part 2: {pt_2_geodes}")
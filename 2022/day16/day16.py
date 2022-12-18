from functools import cache
import time

rates = {}
links = {}
pos_valves = set()
with open('input.txt', "r") as f:
    for line in f.read().splitlines():
        words = line.split(" ")
        valve = words[1]
        rate = int(words[4].split("=")[1].strip(";"))
        linked_valves = "".join([c for c in line.split("valve")[1] if c.isupper()])
        rates[valve] = rate
        links[valve] = [linked_valves[i:i+2] for i in range(0, len(linked_valves), 2)]
        if rate > 0:
            pos_valves.add(valve)

@cache # life saver, memoization FTW
def part_1(curr_valve, time, opened):
    if time <= 1: # Can't do any more opens
        return 0
    best = 0
    
    # Search through all valve paths
    for valve in links[curr_valve]:
        best = max(best, part_1(valve, time - 1, opened))

    # Open valve if it's not already open and it's a positive valve
    if curr_valve not in opened and curr_valve in pos_valves:
        opened = tuple(sorted([*opened, curr_valve])) # Opened needs to be a tuple for cache
        new_rate = rates[curr_valve] * (time - 1)
        best = max(best, part_1(curr_valve, time - 1, opened) + new_rate) 
    return best

tic = time.perf_counter()
print(f"Part 1: {part_1('AA', 30, ())}")
toc = time.perf_counter()
print(f"Part 1 in {toc - tic:0.4f} seconds")

@cache # life saver, memoization FTW
def part_2(curr_valve, time, opened):
    if time <= 1: # Can't do any more opens
        return part_1("AA", 26, opened) # Run elephant simulation with current opened valves
    best = 0
    
    # Search through all valve paths
    for valve in links[curr_valve]:
        best = max(best, part_2(valve, time - 1, opened))

    # Open valve if it's not already open and it's a positive valve
    if curr_valve not in opened and curr_valve in pos_valves:
        opened = tuple(sorted([*opened, curr_valve])) # Opened needs to be a tuple for cache
        new_rate = rates[curr_valve] * (time - 1)
        best = max(best, part_2(curr_valve, time - 1, opened) + new_rate) 
    return best

# For part 2, we can do part 1 once and then do it again to simulate the elephant
tic = time.perf_counter()
print(f"Part 2: {part_2('AA', 26, ())}")
toc = time.perf_counter()
print(f"Part 2 in {toc - tic:0.4f} seconds")

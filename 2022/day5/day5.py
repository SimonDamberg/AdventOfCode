from collections import deque
import re

with open("input.txt", "r") as f:
    start, instr = f.read().split("\n\n")
    rows = start.split("\n")

def parseBoxes(rows):
    # Parse starting state for boxes
    boxes = [deque() for _ in range(len(rows[0]) // 4 + 1)]
    for row in start.split("\n"):
        for i in range(1, len(row), 4):
            tile = row[i]
            if tile != " " and ord(tile) > 60:
                boxes[(i // 4)].append(tile)
    return boxes
        
# Iterate through instructions
def solve(boxes, instr, part1):
    for line in instr.splitlines():
        nums = [int(x) for x in re.findall(r"\d+", line)]
        if part1:
            for _ in range(nums[0]):
                box_to_move = boxes[nums[1]-1].popleft()
                boxes[nums[2]-1].appendleft(box_to_move)
        else:
            boxes_to_move = []
            
            # Get all boxes to move
            for _ in range(nums[0]):
                boxes_to_move.insert(0, boxes[nums[1]-1].popleft())
            
            # Move boxes retaining order
            for box in boxes_to_move:
                boxes[nums[2]-1].appendleft(box)

    return "".join([x[0] for x in boxes])


print(f"Part 1: {solve(parseBoxes(rows), instr, True)}")
print(f"Part 2: {solve(parseBoxes(rows), instr, False)}")
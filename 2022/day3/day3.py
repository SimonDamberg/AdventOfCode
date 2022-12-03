with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# Part 1
part_1 = 0
for line in lines:
    first_half = set(line[:len(line)//2])
    second_half = set(line[len(line)//2:])
    both = first_half.intersection(second_half)
    prio = ord(both.pop()) if both else 0
    part_1 += prio-96 if prio>90 else prio-38

# Part 2
part_2 = 0
for i in range(0, len(lines), 3):
    first = set(lines[i])
    second = set(lines[i+1])
    third = set(lines[i+2])
    three = first.intersection(second, third)
    prio = ord(three.pop()) if three else 0
    part_2 += prio-96 if prio>90 else prio-38

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")

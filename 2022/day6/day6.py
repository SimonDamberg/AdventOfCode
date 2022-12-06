with open("input.txt", "r") as f:
    seq = f.read()

part_1 = 0
for i in range(4, len(seq)):
    if len(set(seq[i-4:i])) == 4:
        part_1 = i
        break
print(f"Part 1: {part_1}")

part_2 = 0
for i in range(14, len(seq)):
    if len(set(seq[i-14:i])) == 14:
        part_2 = i
        break
print(f"Part 2: {part_2}")

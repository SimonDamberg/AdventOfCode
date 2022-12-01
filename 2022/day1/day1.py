# Parse input.txt
elfs = []
with open("input.txt", "r") as f:
    chunks = f.read().split("\n\n")
    for chunk in chunks:
        elfs.append(sum([int(x) for x in chunk.split("\n")]))

# Part 1: Find max elf
max_elf = max(elfs)

# Part 2: Find sum of top 3 elfs
top_elfs = sum(sorted(elfs, reverse=True)[:3])

print(f"Part 1: {max_elf}")
print(f"Part 2: {top_elfs}")
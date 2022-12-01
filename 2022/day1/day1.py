# Parse input.txt
elfs = []
with open("input.txt") as f:
    current_cal = 0
    # Iterate line by line
    for line in f:
        if line == "":
            # EOF
            elfs.append(current_cal)

        line = line.replace("\n", "")
        if line == "":
            # End of current elf
            elfs.append(current_cal)
            current_cal = 0
        else:
            # Still at an elf
            current_cal += int(line)
    f.close()

# Part 1: Find max elf
max_elf = max(elfs)

# Part 2: Find sum of top 3 elfs
top_elfs = sum(sorted(elfs, reverse=True)[:3])

print(f"Part 1: {max_elf}")
print(f"Part 2: {top_elfs}")
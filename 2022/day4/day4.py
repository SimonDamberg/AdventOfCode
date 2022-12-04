import numpy as np

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

contains = 0
overlap = 0
for line in lines:
    first_elf, second_elf = line.split(",")
    first_elf_start, first_elf_end = first_elf.split("-")
    second_elf_start, second_elf_end = second_elf.split("-")
    first, second = np.zeros(99), np.zeros(99)
    
    # Set bits in both elfs
    first[int(first_elf_start)-1:int(first_elf_end)] = 1
    second[int(second_elf_start)-1:int(second_elf_end)] = 1
    
    # AND the two elves
    both = first*second

    # First or second elf contains the other 
    if np.all(both[int(first_elf_start)-1:int(first_elf_end)]) or np.all(both[int(second_elf_start)-1:int(second_elf_end)]):
        contains += 1

    # Check for any overlap 
    if np.any(both):
        overlap += 1

print(f"Part 1: {contains}")
print(f"Part 2: {overlap}")
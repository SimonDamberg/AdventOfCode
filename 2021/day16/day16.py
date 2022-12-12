with open("2021/day16/input.txt", "r") as f:
    binary = bin(int(f.read().strip(), 16))[2:].zfill(4)

# Part 1
version = int(binary[0:3], 2)
type = int(binary[3:6], 2)
print(binary[7:11])
print(binary[12:16])
print(binary[17:21])
value = int(binary[7:11]+binary[12:16] + binary[17:21], 2)
print(version)
print(type)
print(value)
x = 1
cycle = 0
signal = 0
crt = ""
with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal += x * cycle
        if cycle % 40 - 1 in [x-1, x, x+1]:
            crt += "#"
        else:
            crt += "."
        if "noop" == line:
            pass
        else:
            # one cycle to add
            cycle += 1

            if cycle in [20, 60, 100, 140, 180, 220]:
                signal += x * cycle
            if cycle % 40 - 1 in [x-1, x, x+1]:
                crt += "#"
            else:
                crt += "."  
            x += int(line.split(" ")[1])

print(f"Part 1: {signal}")
print("Part 2:")
for i in range(0, len(crt), 40):
    print(crt[i:i+40])
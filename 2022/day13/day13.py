import functools

with open("input.txt", "r") as f:
    pairs = f.read().split("\n\n")

def compare(first, second):
    # Both ints
    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return -1
        elif first > second:
            return 1
        else:
            return 0
    # One is a list, the other is not
    elif isinstance(first, int): # a [b] -> [a] [b]
        return compare([first], second)
    elif isinstance(second, int): # [a] b -> [a] [b]
        return compare(first, [second])
    
    # Both are lists
    elif len(first) > 0 and len(second) > 0: 
        res = compare(first[0], second[0])
        return res if res else compare(first[1:], second[1:])
    
    # Some list has finished
    elif len(first) > 0: 
        return 1
    elif len(second) > 0:
        return -1
    else: 
        return 0

right_pairs = []
packets = [[[2]], [[6]]] # Init array for part 2 with divider packets
for i in range(len(pairs)):
    pair = pairs[i]
    pair = pair.split("\n")
    packets += [eval(pair[0]), eval(pair[1])]

    print(f"Pair {i+1}: {pair[0]} - {pair[1]}")
    if compare(eval(pair[0]), eval(pair[1])) == -1: # Eval to convert to lists
        print("Right")
        right_pairs.append(i+1)
    
print(f"Part 1: {sum(right_pairs)}")

# Use custom compare func with functools.cmp_to_key
packets = sorted(packets, key=functools.cmp_to_key(compare))
idx1 = packets.index([[2]])+1
idx2 = packets.index([[6]])+1
print(f"Part 2: {idx1*idx2}")
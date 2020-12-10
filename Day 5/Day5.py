def decode(code, range):
    for char in code:
        if char == "F" or char == "L":
            diff = range[1] - range[0]
            range[1] = range[1] - (diff // 2) - 1
        else:
            diff = range[1] - range[0]
            range[0] = range[1] - (diff // 2)
    return range[0]

with open("input.txt") as file:
    lines = file.readlines()
    allSeats = []
    for line in lines:
        row = decode(line[:-4], [0, 127])
        seat = decode(line[-4:], [0, 7])
        allSeats.append(row*8 + seat)
    yourSeat = sum(range(min(allSeats), max(allSeats) + 1)) - sum(allSeats)
    print("Part 1: " + str(max(allSeats)))
    print("Part 2: " + str(yourSeat))

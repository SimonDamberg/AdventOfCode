elves = []
new_elves = []
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
with open("input.txt", "r") as f:
    for y, line in enumerate(f.read().split("\n")):
        for x, c in enumerate(line):
            if c == "#":
                elves.append((x, y))
                new_elves.append((x, y))


def count_grid(elves):
    min_x = min(elves, key=lambda x: x[0])[0]
    max_x = max(elves, key=lambda x: x[0])[0]
    min_y = min(elves, key=lambda x: x[1])[1]
    max_y = max(elves, key=lambda x: x[1])[1]
    empty = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in elves:
                print("#", end="")
            else:
                empty += 1
                print(".", end="")
        print()
    return empty

round = 1
while True:
    print(f"Round {round}")
    moved_elves = 0

    # Step one: All elves proposes move
    for i, elf in enumerate(elves):
        # Check if no elf in all directions, even diagonally
        elf_around = False
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if (elf[0]+dx, elf[1]+dy) in elves:
                elf_around = True
                break
        if elf_around:
            for move in moves:
                if abs(move[0]) > 0:
                    # Horizontal move
                    if (elf[0] + move[0], elf[1]) in elves or (elf[0] + move[0], elf[1]+1) in elves or (elf[0] + move[0], elf[1]-1) in elves:
                        # Occupied, try next move
                        continue
                    else:
                        new_elves[i] = (elf[0] + move[0], elf[1])
                        break
                else:
                    # Vertical move
                    if (elf[0], elf[1] + move[1]) in elves or (elf[0]+1, elf[1] + move[1]) in elves or (elf[0]-1, elf[1] + move[1]) in elves:
                        # Occupied, try next move
                        continue
                    else:
                        new_elves[i] = (elf[0], elf[1] + move[1])
                        break

    # Step two: Move all elves with unique positions
    # TODO: Optimize by changing elves to sets, checks go from O(N) to O(1)
    """
    new_positions = list(new_pos.values())
    new_elves = set()
    for elf in new_pos.keys():
        if new_positions.count(new_pos[elf]) == 1:
            elves.remove(elf)
            new_elves.add(new_pos[elf])
            moved_elves += 1
    elves.update(new_elves)
    """

    elves_to_reset = []
    for i, new_elve in enumerate(new_elves):
        if elves[i] == new_elve:
            # No new position
            continue
        
        # Check if new position is unique
        if new_elve not in new_elves[:i] + new_elves[i+1:]:
            moved_elves += 1
            elves[i] = new_elve
        else:
            elves_to_reset.append(i)
    
    for i in elves_to_reset:
        new_elves[i] = elves[i]

    # Step three: move first move to end
    moves.append(moves.pop(0))
    if round == 10:
        print(f"Part 1: {count_grid(elves)}")
    if moved_elves == 0:
        print(f"Part 2: {round}")
        break
    round += 1

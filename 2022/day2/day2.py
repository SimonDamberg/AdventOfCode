rounds = []
with open("input.txt") as f:
    for line in f:
        rounds.append(line.strip().split(" "))

# Part 1
score = 0
for round in rounds:
    if round[1] == "X": # Rock
        score += 1
        if round[0] == "C":
            # Win against Scissors
            score += 6
        elif round[0] == "A":
            # Draw against rock
            score += 3
    elif round[1] == "Y": # Paper
        score += 2
        if round[0] == "A":
            # Win against Rock
            score += 6 
        elif round[0] == "B":
            # Draw against Paper
            score += 3 
    else: # Scissors
        score += 3
        if round[0] == "B":
            # Win against Paper
            score += 6
        elif round[0] == "C":
            # Draw against Scissors
            score += 3
print(f"Part 1: {score}")

# Part 2
score = 0
for round in rounds:
    if round[1] == "X": # Should be loss
        if round[0] == "A": # Rock
            # We pick scissors
            score += 3
        elif round[0] == "B": # Paper
            # We pick rock
            score += 1
        else:
            # We pick paper
            score += 2
    elif round[1] == "Y": # Should be draw
        score += 3
        if round[0] == "A": # Rock
            score += 1
        elif round[0] == "B": # Paper
            score += 2
        else: # Scissors
            score += 3
    else: # Should be win
        score += 6
        if round[0] == "A": # Rock
            # We pick paper
            score += 2
        elif round[0] == "B": # Paper
            # We pick scissors
            score += 3
        else: # Scissors
            # We pick rock
            score += 1
print(f"Part 2: {score}")
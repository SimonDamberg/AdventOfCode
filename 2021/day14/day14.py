with open("day14.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

seq = lines[0]
rules = lines[2:]
rule_dict = {}
for rule in rules:
    rule_dict[rule[0:2]] = rule[6:]

def get_seq(iterations, seq):
    new_seq = seq
    for _ in range(iterations):
        seq = new_seq
        new_seq = seq[0] # reset new_seq
        for i in range(0, len(seq)-1):
            pair = seq[i]+seq[i+1]
            if pair in rule_dict:
                new_seq += rule_dict[pair] + seq[i+1] 

    occurence = {}
    for char in new_seq:
        if char in occurence:
            occurence[char] += 1
        else:
            occurence[char] = 1
    max_occurence = max(occurence.values())
    min_occurence = min(occurence.values())
    return max_occurence-min_occurence

# Count occurence of each char
print(f"Part 1: {get_seq(10, seq)}")
print(f"Part 2: {get_seq(40, seq)}")
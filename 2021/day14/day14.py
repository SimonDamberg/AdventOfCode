import collections

with open("day14.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

seq = lines[0]
rules = lines[2:]
rule_dict = {}
for rule in rules:
    rule_dict[rule[0:2]] = rule[6:]

def get_seq(iterations, seq):
    pairs_counter = collections.Counter()
    char_counter = collections.Counter()

    # Save intial chars to counter
    for c in seq:
        char_counter[c] += 1

    # Save intital pairs to counter
    for i in range(len(seq)-1):
        pairs_counter[seq[i:i+2]] += 1
        
    for _ in range(iterations):
        # Aux counter to keep track of new pairs this iteration
        new_pairs = collections.Counter()
        
        # Check for new pairings 
        for pair, v in pairs_counter.items():
            new_char = rule_dict[pair]

            # Add new pairings to counter            
            new_pairs[pair[0]+new_char] += v
            new_pairs[new_char+pair[1]] += v

            # Add the new character
            char_counter[new_char] += v

        pairs_counter = new_pairs
    
    occ = sorted(char_counter.values())
    return occ[-1] - occ[0]

print(f"Part 1: {get_seq(10, seq)}")
print(f"Part 2: {get_seq(40, seq)}")
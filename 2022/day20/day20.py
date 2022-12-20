import numpy as np

seq = np.array([int(s) for s in open("input.txt", "r").read().splitlines()])
indices = np.arange(len(seq))

def mix(seq, indices, mixes):
    for _ in range(mixes):
        for n in range(len(seq)):
            num = seq[n]
            curr_idx = indices[n]
            new_idx = ((curr_idx + num) % (len(seq)-1))
            
            # Update indices
            indices[indices > curr_idx] -= 1
            indices[indices >= new_idx] += 1
            indices[n] = new_idx
        
    final_seq = np.zeros(len(seq))
    for n in range(len(seq)):
        final_seq[indices[n]] = seq[n]
    return final_seq

pt_1_mix = mix(seq, indices, 1)
zero_idx = np.where(pt_1_mix == 0)[0][0]
res = 0
for num in (1000, 2000, 3000):
    idx = zero_idx
    for n in range(num):
        idx = (idx + 1) % len(seq)
    res += pt_1_mix[idx]
print(f"Part 1: {res}")

indices = np.arange(len(seq))
seq *= 811589153 # add decryption key
pt_2_mix = mix(seq, indices, 10)
zero_idx = np.where(pt_2_mix == 0)[0][0]
res = 0
for num in (1000, 2000, 3000):
    idx = zero_idx
    for n in range(num):
        idx = (idx + 1) % len(seq)
    res += pt_2_mix[idx]
print(f"Part 2: {res}")
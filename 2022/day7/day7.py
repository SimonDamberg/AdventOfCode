from collections import defaultdict
with open("input.txt", "r") as f:
    sizes = defaultdict(int)
    current_dir = ""
    current_dir_parents = []

    for line in f.read().splitlines():
        if line[0] == "$": 
            # user command
            cmd = line.split("$ ")[1]
            if cmd[0:2] == "cd": # only cd command needs to be handled
                if cmd[3:] == "..":
                    current_dir = current_dir_parents.pop() # set current_dir to last parent
                elif cmd[3:] == "/":
                    current_dir = "/" # set current_dir to root
                    current_dir_parents = []
                else:        
                    current_dir_parents.append(current_dir)
                    current_dir += cmd[3:] + "/" # set current_dir to new dir
        else:
            # outputs from ls command
            if line[0:3] != "dir":
                size = int(line.split(" ")[0])
                for d in current_dir_parents + [current_dir]:
                    sizes[d] += size

print(f"Part 1: {sum([s for s in sizes.values() if s <= 100000])}")

min_space_to_remove = 30000000 - (70000000 - sizes["/"])
print(f"Part 2: {min([s for s in sizes.values() if s >= min_space_to_remove])}")
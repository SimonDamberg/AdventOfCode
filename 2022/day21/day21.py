def parse_file():
    nums = {}
    waiting = {}
    root_1, root_2 = "", ""
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            monkey, yelling = line.split(": ")
            if yelling.isnumeric():
                nums[monkey] = float(yelling)
            elif monkey == "root":
                root_1, root_2 = yelling.split(" + ")
            else:
                waiting[monkey] = yelling
    return nums, waiting, root_1, root_2

def get_value(monkey):
    if monkey in nums:
        return nums[monkey]
    else:
        a, op, b = waiting[monkey].split(" ")
        nums[monkey] = eval(f"{get_value(a)} {op} {get_value(b)}")
        return nums[monkey]

nums, waiting, root_1, root_2 = parse_file()
print(f"Part 1: {int(get_value(root_1) + get_value(root_2))}")

def is_humn_in_sequence(root):
    if root == "humn":
        return 1
    else:
        found = 0
        if root in waiting:
            for node in [waiting[root].split(" ")[0], waiting[root].split(" ")[2]]:
                found += is_humn_in_sequence(node)
        return found

def find_humn(wanted, monkey):
    if monkey == "humn":
        return wanted
    elif monkey in nums:
        return nums[monkey]
    else:
        a, op, b = waiting[monkey].split(" ")
        if op == "+":
            if is_humn_in_sequence(a):
                nums[monkey] = find_humn(wanted-get_value(b), a)
            else:
                nums[monkey] = find_humn(wanted-get_value(a), b)
        elif op == "-":
            if is_humn_in_sequence(a):
                nums[monkey] = find_humn(wanted+get_value(b), a)
            else:
                nums[monkey] = find_humn(get_value(a)-wanted, b)
        elif op == "*":
            if is_humn_in_sequence(a):
                nums[monkey] = find_humn(wanted/get_value(b), a)
            else:
                nums[monkey] = find_humn(wanted/get_value(a), b)
        else:
            if is_humn_in_sequence(a):
                nums[monkey] = find_humn(wanted*get_value(b), a)
            else:
                nums[monkey] = find_humn(get_value(a)/wanted, b)
        return nums[monkey]

nums, waiting, root_1, root_2 = parse_file()
if is_humn_in_sequence(root_1):
    wanted, root = get_value(root_2), root_1
else:
    wanted, root = get_value(root_1), root_2
print(f"Part 2: {int(find_humn(wanted, root))}")
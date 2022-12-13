import math

def parse_input():
    monkeys = []
    with open('input.txt') as f:
        lines = f.read().strip().split("Monkey ")
        for i in range(1, len(lines)):
            monkey = {"inspected": 0}
            info = lines[i].split("\n")
            monkey["items"] = [int(x) for x in info[1].split(": ")[1].split(", ")]
            monkey["op"] = info[2].split("new = ")[1]
            monkey["test"] = int(info[3].split("by ")[1])
            monkey["true"] = int(info[4].split("monkey ")[1])
            monkey["false"] = int(info[5].split("monkey ")[1])
            monkeys.append(monkey)
    return monkeys

def perform_op_part_1(worry, op):
    if "old" == op[6:]:
        x = worry
    else:
        x = int(op[6:])

    if "*" in op:
        return math.floor((worry * x) / 3)
    else:
        return math.floor((worry + x) / 3)

def perform_op_part_2(worry, op, lcm):
    # Parse X
    if "old" == op[6:]:
        x = worry
    else:
        x = int(op[6:])

    # Perform operation
    if "*" in op:
        return (worry * x) % lcm
    else:
        return (worry + x) % lcm

# Part 1
pt_1 = parse_input()
for n in range(20):
    for monkey in pt_1:
        for worry in monkey["items"]:
            monkey["inspected"] += 1
            new_worry = perform_op_part_1(worry, monkey["op"])
            if new_worry % monkey["test"] == 0:
                pt_1[monkey["true"]]["items"].append(new_worry)
            else:
                pt_1[monkey["false"]]["items"].append(new_worry)
        monkey["items"] = []

# Get monkeys with two most inspections
pt_1.sort(key=lambda x: x["inspected"], reverse=True)
print(f'Part 1: {pt_1[0]["inspected"] * pt_1[1]["inspected"]}')

# Part 2: Divide each worry with the LCM of all tests since it ensures same divisibility
pt_2 = parse_input()
lcm = 1
for monkey in pt_2:
    lcm = lcm * monkey["test"] // math.gcd(lcm, monkey["test"])

for n in range(10000):
    for monkey in pt_2:
        for worry in monkey["items"]:
            monkey["inspected"] += 1
            new_worry = perform_op_part_2(worry, monkey["op"], lcm)
            if new_worry % monkey["test"] == 0:
                pt_2[monkey["true"]]["items"].append(new_worry)
            else:
                pt_2[monkey["false"]]["items"].append(new_worry)
        monkey["items"] = []

# Get monkeys with two most inspections
pt_2.sort(key=lambda x: x["inspected"], reverse=True)
print(f'Part 2: {pt_2[0]["inspected"] * pt_2[1]["inspected"]}')

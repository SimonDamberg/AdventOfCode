def parseInput():
    with open("test.txt") as file:
        lines = file.readlines()
    commands = []
    for line in lines:
        operation = line.split(" ")[0]
        value = line.split(" ")[1].rstrip()
        commands.append((operation, value))
    return commands

def executePart1(commands):
    accumulator = 0
    executedCommands = []
    i = 0
    while True:
        command = commands[i]
        if i in executedCommands:
            break
        executedCommands.append(i)
        if command[0] == "acc":
            accumulator += int(command[1])
            i+=1
        elif command[0] == "jmp":
            value = command[1]
            if value[0] == "+":
                i += int(value[1:])
            else:
                i -= int(value[1:])
        else:
            i+=1
    return accumulator

def executePart2(commands):
    accumulator = 0
    executedCommands = []
    hasNotChanged = True
    i = 0
    while True:
        try:
            command = commands[i]
            print(command)
            executedCommands.append(i+1)
            if command[0] == "acc":
                accumulator += int(command[1])
                i+=1
            elif command[0] == "jmp":
                value = command[1]
                if value[0] == "+":
                    if i+int(value[1:]) in executedCommands and hasNotChanged:
                        print("jmp to nop")
                        commands[i] = ("nop", value)
                        i+=1
                        hasNotChanged = False
                    else:
                        i += int(value[1:])
                else:
                    if i-int(value[1:]) in executedCommands and hasNotChanged:
                        print("jmp to nop")
                        commands[i] = ("nop", value)
                        i+=1
                        hasNotChanged = False
                    else:
                        i -= int(value[1:])
            else:
                value = command[1]
                if value[0] == "+":
                    if i+int(value[1:]) not in executedCommands and hasNotChanged:
                        print("nop to jmp")
                        print(commands[i])
                        commands[i] = ("jmp", value)
                        print(commands[i])
                        i += int(value[1:])
                        hasNotChanged = False
                    else:
                        i+=1
                else:
                    if i-int(value[1:]) not in executedCommands and hasNotChanged:
                        print("nop to jmp")
                        commands[i] = ("jmp", value)
                        i -= int(value[1:])
                        hasNotChanged = False
                    else:
                        i+=1
        except:
            return accumulator

commands = parseInput()
print("Part 1: " + str(executePart1(commands)))
print("Part 2: " + str(executePart2(commands)))

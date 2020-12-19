

def parsePart1():
    rules = {}
    with open("input.txt") as file:
        lines = file.readlines()
    for line in lines:
        currentBag = " ".join(line.split(" ")[:2])
        contents = line.split("contain")[1].split(",")
        colours = []
        for bag in contents:
            colours.append(" ".join(bag.split(" ")[2:4]))
        rules[currentBag] = colours
    return rules


def parsePart2():
    rules = {}
    with open("test.txt") as file:
        lines = file.readlines()
    for line in lines:
        currentBag = " ".join(line.split(" ")[:2])
        contents = line.split("contain")[1].split(",")
        subBags = {}
        for bag in contents:
            if(bag[1].isdigit()):
                subBags[" ".join(bag.split(" ")[2:4])] = bag[1]
        rules[currentBag] = subBags
    return rules

def containsShinyGold(bag):
    try:
        subBags = rules[bag]
        for subBag in subBags:
            if subBag == "shiny gold" or containsShinyGold(subBag):
                return True
        return False
    except:
        return False

def totalBagsInside(bag):
    try:
        subBags = rules[bag]
        print(str(bag) + ": " + str(subBags))
        count = 0
        for colour, amount in subBags.items():
            count = count + (int(amount)*totalBagsInside(colour))
        return count
            #count += v #+ totalBagsInside(sub)
    except:
        return 0


#Part 1
rules = parsePart1()
part1 = 0
for bag in rules:
    if containsShinyGold(bag):
        part1 += 1

#Part 2
rules = parsePart2()
part2 = totalBagsInside("shiny gold")

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))

with open("input.txt") as file:
    lines = file.readlines()

rules = {}
occurences = []

#Counts as 2 ways if a bag contains 2 other bags that contains a shiny gold one
def getContents(bag):
    try:
        content = rules[bag]
        for result in content:
            if "shiny gold" in result:
                occurences.append(result)
            else:
                getContents(result)
    except:
        pass

for line in lines:
    currentBag = " ".join(line.split(" ")[:2])
    contents = line.split("contain")[1].split(",")
    colours = []
    for bag in contents:
        colours.append(" ".join(bag.split(" ")[2:4]))
    rules[currentBag] = colours

for rule in rules:
    getContents(rule)
print(len(occurences))

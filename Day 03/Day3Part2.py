def traverse(sideSteps, downSteps):
    with open("day3.txt", "r") as file:
        totalTrees = 0
        currentPosition = sideSteps
        firstLine = file.readline() # Skip first line
        lineSize = len(firstLine)-2 #Remove \n and get index instead of size
        for line in file: #Loop through all lines
            for i in range(downSteps-1):
                line = file.readline()
            if line[currentPosition] == "#":
                totalTrees+=1
            if currentPosition+sideSteps > lineSize:
                currentPosition = currentPosition + sideSteps - lineSize - 1
            else:
                currentPosition+=sideSteps
    return totalTrees

sum = traverse(1, 1)*traverse(3, 1)*traverse(5, 1)*traverse(7, 1)*traverse(1,2)
print(sum)

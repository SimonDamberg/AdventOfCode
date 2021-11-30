with open("day3.txt", "r") as file:
    totalTrees = 0
    currentPosition = 3 # Start at 3 since we skip the first line
    firstLine = file.readline() # Skip first line
    lineSize = len(firstLine)-2 #Remove \n and get index instead of size
    for line in file: #Loop through all lines 
        if line[currentPosition] == "#":
            totalTrees+=1
        if currentPosition+3 > lineSize:
            currentPosition = currentPosition + 3 - lineSize - 1
        else:
            currentPosition+=3
    print(totalTrees)

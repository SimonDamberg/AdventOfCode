requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
noValidPassports = 0

with open("input.txt") as file:
    currentBatch = ""
    for line in file:
        if line == "\n":
            currentBatch = currentBatch.rstrip().split()
            presentFields = []
            for field in currentBatch:
                presentFields.append(field.split(":")[0])
            try:
                presentFields.remove("cid")
            except:
                pass
            if len(presentFields) == len(requiredFields):
                noValidPassports += 1
            currentBatch = ""
        else:
            currentBatch += line
    #Do again since it skips the last.
    #Bad implementation but don't know how to check if line is the last one
    currentBatch = currentBatch.rstrip().split()
    presentFields = []
    for field in currentBatch:
        presentFields.append(field.split(":")[0])

    try:
        presentFields.remove("cid")
    except:
        pass
    if len(presentFields) == len(requiredFields):
        noValidPassports += 1

    print(noValidPassports)

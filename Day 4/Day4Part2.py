requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
noValidPassports = 0

def checkValidField(field, value):
    if field == "byr":
        return value >= 1920 and value <= 2002
    elif field == "iyr":
        return value >= 2010 and value <= 2020
    elif field == "eyr":
        return value >= 2020 and value <= 2030
    #elif field == "hgt":
    #???
    #    isValid == help
    #elif field == "hcl": # ???
    #    isValid = isValid && value >= 2020 && value <= 2030
    elif field == "ecl": #
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return len(value)==9

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
                isValid = True;
                for n in range(len(presentFields)):
                    currField = presentFields[n]
                    value = currentBatch[n].split(":")[1]
                    print(value)
                    isValid = isValid and checkValidField(currField, value)
                if isValid:
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

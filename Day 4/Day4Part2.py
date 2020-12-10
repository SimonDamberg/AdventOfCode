requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
noValidPassports = 0

# Veru ugly, worst implementation yet
def checkValidField(field, value):
    if field == "byr":
        return int(value) >= 1920 and int(value) <= 2002
    elif field == "iyr":
        return int(value) >= 2010 and int(value) <= 2020
    elif field == "eyr":
        return int(value) >= 2020 and int(value) <= 2030
    elif field == "hgt":
        metric = value[-2:]
        if metric == "cm":
            return int(value[:-2]) >= 150 and int(value[:-2]) <= 193
        elif metric == "in":
            return int(value[:-2]) >= 59 and int(value[:-2]) <= 76
        else:
            return False
    elif field == "hcl":
        metric = value[0]
        if metric == "#":
            if len(value[1:]) == 6:
                allValid = True
                for char in value[1:]:
                    digitValid = char.isdigit() and int(char) >= 0
                    charValid = char in ["a", "b", "c", "d", "e", "f"]
                    validChar = digitValid or charValid
                    allValid = allValid and validChar
                return allValid
            else:
                return False
        else:
            return False
    elif field == "ecl": #
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        isValid = len(value)==9
        for num in value:
            isValid = isValid and num.isdigit()
        return isValid

with open("input.txt") as file:
    currentBatch = ""
    for line in file:
        if line == "\n":
            currentBatch = currentBatch.rstrip().split()
            presentFields = []
            for field in currentBatch:
                if "cid" not in field.split(":")[0]:
                    presentFields.append(field)
            if len(presentFields) == len(requiredFields):
                isValid = True;
                for n in range(len(presentFields)):
                    currField = presentFields[n].split(":")[0]
                    value = presentFields[n].split(":")[1]
                    isValid = isValid and checkValidField(currField, value)
                if isValid == True:
                    noValidPassports += 1

            currentBatch = ""
        else:
            currentBatch += line
    #Do again since it skips the last. Bad implementation
    currentBatch = currentBatch.rstrip().split()
    presentFields = []
    for field in currentBatch:
        if "cid" not in field.split(":")[0]:
            presentFields.append(field)
    if len(presentFields) == len(requiredFields):
        isValid = True;
        for n in range(len(presentFields)):
            currField = presentFields[n].split(":")[0]
            value = presentFields[n].split(":")[1]
            isValid = checkValidField(currField, value)
        if isValid == True:
            noValidPassports += 1

    print(noValidPassports)

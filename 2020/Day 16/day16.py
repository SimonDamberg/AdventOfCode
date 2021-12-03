lines = open("test.txt").readlines()
fields = [] # List of tuples of tuple with ((min max), (min max))
invalid_numbers = []

for line in lines:
    line = line.replace("\n", "")
    if ":" in line and "your" not in line and "nearby" not in line:
        line = line.split(": ")[1]
        line = line.split(" or ")
        # Get min max from row: 6-11 or 33-44
        fields.append(((int(line[0].split("-")[0]), int(line[0].split("-")[1])), (int(line[1].split("-")[0]), int(line[1].split("-")[1]))))
start_index = lines.index("nearby tickets:\n")
lines = lines[start_index+1:]
for line in lines:
    line = line.replace("\n", "")
    numbers = line.split(",")
    # check if every number is valid for atleast one field
    for number in numbers:
        valid = False
        for field in fields:
            if int(number) >= field[0][0] and int(number) <= field[0][1] or int(number) >= field[1][0] and int(number) <= field[1][1]:
                valid = True
        if not valid:
            invalid_numbers.append(int(number))
print(sum(invalid_numbers))

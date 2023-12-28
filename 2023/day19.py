from submit_if_correct import submit_if_correct
YEAR = 2023 

# ------------------ #
DAY = 19 # CHANGE THIS
# ------------------ #

def parse_ratings(input):
    ratings = []
    for line in input.splitlines():
        rating = {}
        line = line.replace("{", "").replace("}", "")
        for pair in line.split(","):
            field, value = pair.split("=")
            rating[field] = int(value)
        ratings.append(rating)
    return ratings

def parse_workflows(input):
    workflows = {}
    for line in input.splitlines():
        workflow_rules = []
        workflow_name = line.split("{")[0]
        rules = line.split("{")[1].split("}")[0].split(",")
        for rule in rules:
            # Split either on > or <
            if ">" in rule:
                condition = ">"
                field, value = rule.split(">")
            elif "<" in rule:
                condition = "<"
                field, value = rule.split("<")
            else:
                # no condition, this is the output
                workflow_rules.append({
                    "field": "otherwise",
                    "output": rule
                })
                continue

            value, output = value.split(":")
            workflow_rules.append({
                "field": field,
                "condition": condition,
                "value": int(value),
                "output": output
            })
        workflows[workflow_name] = workflow_rules
    return workflows

def solve_part_1(input, test_case=True):
    # -------------PART 1------------- #
    TRUE_ANSWER = 19114
    workflows, ratings = input.split("\n\n")
    ratings = parse_ratings(ratings)
    workflows = parse_workflows(workflows)  

    accepted = []
    stack = [("in", x) for x in ratings]
    while stack:
        w, r = stack.pop() # workflow and ratings to process
        if w == "A": # accept, add to accepted
            accepted.append(r)
            continue
        elif w == "R": # reject, skip
            continue
        else:
            for check in workflows[w]: # check each rule
                field = check["field"]
                if field == "otherwise":
                    stack.append((check["output"], r))
                    break
                elif check["condition"] == ">":
                    if r[field] > check["value"]:
                        stack.append((check["output"], r))
                        break
                elif check["condition"] == "<":
                    if r[field] < check["value"]:
                        stack.append((check["output"], r))
                        break
                else:
                    raise ValueError(f"Unknown condition {check['condition']}")

    # sum up values in accepted ratings
    answer = 0
    for ratings in accepted:
        answer += sum(ratings.values())

    if test_case:
        print(f'(TEST) Part 1: {answer}')
        submit_if_correct(solve_part_1, answer, TRUE_ANSWER, DAY, 1, YEAR)
    else:
        print(f'(REAL) Part 1: {answer}')
    return answer

def size_of_range(ranges):
    size = 1
    for range in ranges.values():
        size *= (1 + range[1] - range[0])
    return size

def find_accepted_combinations(workflows, ranges, current):
    rules = workflows[current]
    accepted = 0
    for rule in rules:
        # We iterate through each rule for current workflow, updating the working ranges as we go

        if rule["field"] == "otherwise": # if no conditions to check
            if rule["output"] == "A":
                accepted += size_of_range(ranges)
            elif rule["output"] != "R": # if not reject, continue
                accepted += find_accepted_combinations(workflows, ranges, rule["output"])
        else:
            (min_field_val, max_field_val) = ranges[rule["field"]]

            if rule["condition"] == "<":
                if min_field_val < rule["value"]:
                    new_ranges = ranges.copy() # copy ranges so we can update them without affecting other rules
                    new_ranges[rule["field"]] = (min_field_val, min(max_field_val, rule["value"]-1)) # update range as if check passed
                    
                    if rule["output"] == "A": # if accept, add size of range
                        accepted += size_of_range(new_ranges)
                    elif rule["output"] != "R": # if not reject, recurse
                        accepted += find_accepted_combinations(workflows, new_ranges, rule["output"])
                #ranges[rule["field"]] = (rule["value"], max_field_val) # update range as if check failed for next rule 
            else:
                if max_field_val > rule["value"]:
                    new_ranges = ranges.copy() # copy ranges so we can update them without affecting other rules
                    new_ranges[rule["field"]] = (max(min_field_val, rule["value"]+1), max_field_val) # update range as if check passed
                    
                    if rule["output"] == "A": # if accept, add size of range
                        accepted += size_of_range(new_ranges)
                    elif rule["output"] != "R": # if not reject, recurse
                        accepted += find_accepted_combinations(workflows, new_ranges, rule["output"])
                
                #ranges[rule["field"]] = (min_field_val, rule["value"]) # update range as if check failed for next rule
    return accepted


def solve_part_2(input, test_case=True):
    # -------------PART 2------------- #
    TRUE_ANSWER = 167409079868000
    workflows, _ = input.split("\n\n")
    workflows = parse_workflows(workflows)  
    ranges = {}
    for val in "xmas":
        ranges[val] = (1, 4000)

    answer = find_accepted_combinations(workflows, ranges, "in")

    if test_case:
        print(f'(TEST) Part 2: {answer}')
        submit_if_correct(solve_part_2, answer, TRUE_ANSWER, DAY, 2, YEAR)
    else:
        print(f'(REAL) Part 2: {answer}')
    return answer

part1=open(f"ex_inputs/day{DAY}/1.txt","r")
solve_part_1(part1.read(), test_case=True)
part2=open(f"ex_inputs/day{DAY}/2.txt","r")
solve_part_2(part2.read(), test_case=True)
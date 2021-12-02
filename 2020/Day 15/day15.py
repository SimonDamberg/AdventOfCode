numbers = [5,2,8,16,18,0,1]
for i in range(7, 2020):
    prev_spoken = numbers[i - 1]
    try:
        reversed_list = list(reversed(numbers[:-1]))
        index_last_occurence = len(numbers) - reversed_list.index(prev_spoken) - 1
    except ValueError:
        numbers.append(0)
        continue
    age = i - index_last_occurence
    numbers.append(age)
print(numbers[-1])
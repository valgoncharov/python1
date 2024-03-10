# Example
all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = []

for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)

print(all_nums)

# Example for LIST
all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = [abs(num) for num in all_nums]

print(absolute_nums)

print(all_nums)

# Example for filter
all_nums = [-3, 1, 0, 10, -20, 5]

positive_nums = []

for num in all_nums:
    if num > 0:
        positive_nums.append(num)

print(positive_nums)

print(all_nums)

# Example for filter LIST
all_nums = [-3, 1, 0, 10, -20, 5]

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)

print(all_nums)


# Example for SET
my_set = {1, 10, 15}

new_set = set()

for val in my_set:
    new_set.add(val * val)

print(new_set)

print(my_set)

# Example for short
my_set = {1, 10, 15}

new_set = {val * val for val in my_set}

print(new_set)

print(my_set)

# Example for DICT
my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}

score = {}

for key, value in my_scores.items():
    score[key] = value * 10

print(score)

print(my_scores)

# Example short
my_scores1 = {
    'a': 5,
    'b': 3,
    'm': 22
}

score = {key: value * 10 for key, value in my_scores1.items()}
print(score)
print(type(score))

print(my_scores1)
# Exampel SET
score1 = {value * 10 for key, value in my_scores1.items()}
print(score1)
print(type(score1))
# Example LIST
score2 = [value * 10 for key, value in my_scores1.items()]
print(score2)
print(type(score2))

# Example LIST to DICT
my_scores3 = [10, 7, 14]

score3 = {k: v for k, v in enumerate(my_scores3)}

print(score3)
print(type(score3))

score4 = {index: elem * 2 for index, elem in enumerate(my_scores3)}

print(score4)
print(type(score4))

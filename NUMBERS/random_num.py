import random

print(random.random())
print(random.randint(1, 10))

print(random.choice('abcd'))
print(random.choice([1, 5, 33, 0]))

print(random.choices([1, 5, 33, 0, 65], k=2))

print(random.shuffle([1, 5, 33, 0, 65]))
print(random.shuffle([1, 5, 33, 0, 65]))

my_list = [1, 5, 33, 0, 65]
random.shuffle(my_list)
print(my_list)
random.shuffle(my_list)
print(my_list)

print(''.join(random.choices('ABCDEF0123456789', k=2)))

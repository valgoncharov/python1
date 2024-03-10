my_fruits = ['apple', 'banana', 'lime']

my_apple = my_fruits[0]
my_banana = my_fruits[1]
my_lime = my_fruits[2]

print(my_apple)
print(my_banana)
print(my_lime)

my_apple, my_banana, my_lime = my_fruits

# Распаковка списка
my_list = [1, 2, 3]
print(type(my_list))

first, second, third = my_list

print(first)
print(second)
print(third)

# Распаковка кортежа
my_fruits1 = ('apple', 'banana', 'lime')
print(type(my_fruits1))

my_apple1, my_banana1, my_lime1 = my_fruits1

print(my_apple1)
print(my_banana1)
print(my_lime1)


# Распаковка при использовании *
my_fruits2 = ['apple', 'banana', 'lime']

my_apple2, *remaining_fruits = my_fruits2

print(my_apple2)
print(remaining_fruits)
print(type(remaining_fruits))

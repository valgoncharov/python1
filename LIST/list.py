my_fruits = ['apple', 'banana', 'lime']
posts_ids = [151, 245, 762, 167]
user_inputs = [True, 'hi!', ';)', 10.5]

empty_list = []
print(len(empty_list))

print(posts_ids[0])

posts_ids[1] = 23
print(posts_ids)

print(len(user_inputs))

del user_inputs[1]
print(user_inputs)

users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]

print(len(users))

print(users[1]['user_id'])

# Использование переменных
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]

print(all_fruits)

# Несуществующие элементы
# Выше есть

# print(posts_ids[10])

# Метод append
happy_smile = []

happy_smile.append(':-)')
happy_smile.append(':-)')
happy_smile.append(':-p')

print(happy_smile)
print(len(happy_smile))

# Метод POP
inputs = [True, 'hi!', ':-)', 10.5]

inputs.pop()
print(inputs)

inputs.pop(0)
print(inputs)

removed_element = inputs.pop()
print(removed_element)

print(inputs)

# Метод SORT
posts_ids.sort()
print(posts_ids)

posts_ids.sort(reverse=True)
print(posts_ids)

# Конвертация в список
greeting = "Hello from Python"
greeting_lettrs = list(greeting)

print(greeting_lettrs)

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)

print(my_dict_keys)

# Арифметические опреации в списках
ratings = [2.5, 5.0, 4.3, 3.7]

print(min(ratings))
print(max(ratings))
print(sum(ratings))

print(sum(ratings)/len(ratings))

# Объединение списков
my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings
print(all_ratings)

# Нарезка списков
first_two_ratings = ratings[:2]
print(first_two_ratings)

middle_ratings = ratings[1:-1]
print(middle_ratings)

last_two_ratings = ratings[-2:]
print(last_two_ratings)

new_ratings = ratings[:]
print(new_ratings)

# Копирование списков
my_cars = ['BMW', 'Mercedes']

copied_cars = my_cars

copied_cars.append('Audi')

print(copied_cars)

print(my_cars)
print(id(my_cars) == id(copied_cars))
# Копирование в новый список
# Создание нового списка используя slice (нарезка)
copied_cars1 = my_cars[:]

copied_cars1.append('Audi')

print(copied_cars1)

print(my_cars)

print(id(my_cars) == id(copied_cars1))

# Копирование используя copy
copied_cars2 = my_cars.copy()

copied_cars2.append('Audi')

print(copied_cars2)

print(my_cars)

print(id(my_cars) == id(copied_cars2))

# Копирование используя list

copied_cars3 = list(my_cars)

copied_cars3.append('Audi')

print(copied_cars3)

print(my_cars)

print(id(my_cars) == id(copied_cars3))

# Практика
my_nums = [10, 50, 0, 5, 5, 100]

# print(dir(my_nums))
res = my_nums.count(5)
print(res)

apd = my_nums.append(25)
print(my_nums)

inserts = my_nums.insert(2, -5)
print(my_nums)

# my_nums.clear()
# print(my_nums)

my_nums.extend('abc')
print(my_nums)

other_nums = my_nums

print(id(my_nums))
print(id(other_nums))

other_nums = my_nums.copy()

my_nums.append(3)
other_nums.clear()

print(id(my_nums))
print(id(other_nums))

print(my_nums, other_nums)

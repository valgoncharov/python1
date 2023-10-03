my_nums = (10, 5, 100, 0)

print(type(my_nums))

# my_nums[1] = 7 будет ошибка

# del my_nums[1] будет ошибка

users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])

users[1]['user_id'] = 100

print(users[1]['user_id'])

# Использование переменных в кортежах
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = (my_fruit, other_fruit, new_fruit)

print(all_fruits)

# Получение несуществующих элементов

posts_ids = (151, 245, 762, 167)

# print(posts_ids[10])  # будет ошибка IndexError

# Объединение кортежей
internal_id = (151, 245)
external_ids = (624, 451, 941)

all_ids = internal_id + external_ids
print(all_ids)  # Метод __add__

# Метода кортежей count и index

print(posts_ids.count(245))

print(posts_ids.index(245))

# Конвертация в список

posts_ids_list = list(posts_ids)
posts_ids_list.append(351)

print(posts_ids_list)

posts_ids_tuple = tuple(posts_ids_list)

print(posts_ids_tuple)

# Практика
my_num1 = (10, 5, 100, 0, 5, 5)

index_one = my_num1.index(5)
index_two = my_num1.index(5, index_one + 1)
index_three = my_num1.index(5, index_one + 1)

print(index_three)

my_list = list(my_num1)

my_list.append(7)

print(my_list)
print(my_num1)

my_num1 = tuple(my_list)

print(my_num1)

my_touple = tuple('abcd')
my_touple1 = tuple({'a': 1, 'b': True})

print(my_touple)
print(my_touple1)

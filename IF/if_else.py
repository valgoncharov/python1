# my_number = 25
# if my_number > 0:
#     print(my_number, "is positive number")

# # Example if not
# person_info = {
#     'age': 20
# }

# if not person_info.get('name'):
#     # Действия в случаях, если:
#     # 1. Ключа "name" у объекта "person" нет
#     # 2. Ключ "name" есть, но его значение ложно
#     print("Имя отсутствует")

# if 10 > 2:
#     print(True)

# if 10 > 2:
#     print(True)

num_one = 10
num_two = 5.3

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
        isinstance(num_two, int)):
    # Будет пустой вывод из-за 5.3 оно флоат
    print("Both numbers are ints and positive")

# if...else
my_number = 25.5

if type(my_number) is int:
    print(my_number, "is integer")
else:
    print(my_number, "is not an integer")

my_phone = {
    'price': 200,
    # 'brand': 'Nokia'
}

if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")

# if...elif

my_num = -10

if my_num > 0:
    print(my_num, "is positive number")
elif my_num < 0:
    print(my_num, "is negative number")
else:
    print(my_num, "is zero")

# Use if in function


# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "Один из аргументов не целое число"

#     if a >= b:
#         return f"{a} больше или равно {b}"

#     return f"{a} меньше {b}"


def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "Один из аргументов не целое число"
    elif a >= b:
        info = f"{a} больше или равно {b}"
    else:
        info = f"{a} меньше {b}"
    return info


print(nums_info(True, 10))
# Один из аргументов не целое число
print(nums_info(10, 2))  # 10 больше или равно 2
print(nums_info(4, 15))  # 4 меньше 5

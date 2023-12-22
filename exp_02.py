a = (1, 2, 3)
b = a

print(a)
print(b)

print(a.__eq__(b))

print(a is b)

print(2 in a)
print(4 in b)

not 10  # False
not 0  # True
not 'abc'  # False
not ''  # True
not True  # False
not None  # True

not not 10  # True
not not 0  # False
not not 'abc'  # True
not not ''  # False
not not True  # True
not not None  # False

# Exampl

my_list = [1, 2]

other_list = ['a', 'b']

my_dict = {}
my_dict1 = {'a': 5}

print(not not my_list)

print(my_list or other_list)
print(my_list and my_dict)

print(bool(my_list and my_dict))
print(bool(my_list and my_dict1))

print(len(my_list) > 0 or other_list)
print(len(my_list) < 0 or other_list)

my_list2 = []

my_list2 and print("List is not empty")  # Вернет пустой ответ

my_list1 = [1, 2]

my_list1 and print("List is not empty")

my_dict2 = {'a': 1, 'b': 2}
my_dict3 = {'b': 1, 'a': 2}

print(my_dict2 and my_dict3)
my_dict2 and my_dict3 and print("Dictionary are equal")

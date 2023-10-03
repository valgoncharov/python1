my_disk = {}
# print(id(my_disk))
# print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 59

# print(my_disk)
# print(id(my_disk))

# print(my_disk.__doc__)
print(my_disk.items())  # Выводит кортеж
print(my_disk.keys())
# Удаляет один из элементов, добавленный последним
# print(my_disk.popitem())
print(list(my_disk.keys()))  # Можно сделать список

print(my_disk.get('type'))

# Копирование словаря
new_disk = my_disk.copy()
new_disk['type'] = 'SSD'
print(new_disk)
print(id(my_disk))
print(id(new_disk))
print(len(new_disk))

# Конвертация
my_list = [0, True, 'abc']

# my_dict = dict(my_list)

# print(my_dict)  # Ошибка
# Но, если создать список списка, все ок
new_list = [['first', 0], ['second', True]]

new_dict = dict(new_list)

print(new_dict)

# Задача
hw_dict = {}
key1_1 = input('Введите название ключа: ')
key1_2 = input('Введите значение ключа: ')
key2_1 = input('Введите название ключа: ')
key2_2 = input('Введите значение ключа: ')
key3_1 = input('Введите название ключа: ')
key3_2 = input('Введите значение ключа: ')

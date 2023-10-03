fruits = ['apple', 'banana', 'lime']

quantities = [100, 70, 50]

fruit_qtys_zip = zip(fruits, quantities)

print(fruit_qtys_zip)

# fruit_qtys_list = list(fruit_qtys_zip)
# print(fruit_qtys_list)

print(type(fruit_qtys_zip))

availability = [True, False, True]
ava = '1234'
fruit_qtys_zip = zip(fruits, quantities, availability, ava)
fruit_qtys_list = list(fruit_qtys_zip)
print(fruit_qtys_list)

# Конвертация zip в dict
fruit_qtys_zip = zip(fruits, quantities)
fruit_qtys_zip1 = zip(fruits, ava)
fruit_qtys_zip2 = zip(fruits, availability)
dict_fruits = dict(fruit_qtys_zip)
dict_fruits1 = dict(fruit_qtys_zip1)
dict_fruits2 = dict(fruit_qtys_zip2)
print(dict_fruits)
print(dict_fruits1)
print(dict_fruits2)

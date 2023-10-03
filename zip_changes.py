from copy import deepcopy
my_num = 10
other_num = 10

print(id(my_num))
print(id(other_num))

first_num = 10
second_num = first_num

print(id(first_num))
print(id(second_num))

second_num += 5
print(second_num)
print(first_num)

print(id(second_num))
print(id(first_num))

# Адреса изменяемых обьектов
my_list = [1, 2, 3]
print(id(my_list))

other_list = [1, 2, 3]
print(id(other_list))

print(id([1, 2, 3]))

other_list.append(4)

print(my_list)

print(other_list)
print(id(other_list))

# Словари
info = {
    'name': 'Val',
    'is_instructor': True
}

info_copy = info  # Копируем только ссылку

info['reviews_qty'] = 5

print(info['reviews_qty'])

print(info_copy['reviews_qty'])

info_copy['reviews_qty'] = 100

print(info['reviews_qty'])
print(info_copy['reviews_qty'])

# Тут данные будут меняться независимо друг от друга
my_info = {
    'name': 'Val',
    'is_instructor': True
}

other_info = {
    'name': 'Val',
    'is_instructor': True
}

print(id(my_info))
print(id(other_info))

# Как же избежать изменений копий
info1_copy = info.copy()

info1_copy['reviews_qty'] = 5

print(info1_copy)

print(info)

new_info = {
    'name': 'Val',
    'is_instructor': True,
    'reviews': []
}

new_info_copy = new_info.copy()
new_info_copy['reviews'].append('Great course!')

print(new_info)

print(new_info_copy)


new_info1 = {
    'name': 'Val',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(new_info1)

info_deepcopy['reviews'].append('Great course!')

print(new_info1)

print(info_deepcopy)

# Практика

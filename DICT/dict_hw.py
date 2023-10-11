hw_dict = {}
key1_1 = input('Введите название ключа: ')
key1_2 = input('Введите значение ключа: ')
key2_1 = input('Введите название ключа: ')
key2_2 = input('Введите значение ключа: ')
key3_1 = input('Введите название ключа: ')
key3_2 = input('Введите значение ключа: ')

hw_dict[key1_1] = key1_2
hw_dict[key2_1] = key2_2
hw_dict[key3_1] = key3_2

print(hw_dict)

del hw_dict[key1_1]
print(hw_dict)

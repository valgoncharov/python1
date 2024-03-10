# Создаем список словарей
list_of_dicts = [
    {'key1': 'value1', 'key2': 'value2'},
    {'key3': 'value3', 'key4': 'value4'},
    {'key5': 'value5', 'key6': 'value6'}
]

# Используем оператор распаковки списков для создания переменных
dict1, dict2, dict3 = list_of_dicts

# Выводим содержимое переменных
print("Первый словарь:", dict1)
print("Второй словарь:", dict2)
print("Третий словарь:", dict3)


def my_function(arg1, arg2):
    # Выводим значения аргументов
    print("Аргумент 1:", arg1)
    print("Аргумент 2:", arg2)


# Вызываем функцию и распаковываем словари в аргументах
my_function(*list_of_dicts)

# Вызываем функцию трижды с разными словарями
my_function(*list_of_dicts[0])
my_function(*list_of_dicts[1])
my_function(*list_of_dicts[2])

# Example
my_motobike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

other_motobike = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati'
}
# При сравнении они технически одинаковы, но ссылки разные в памяти
print(my_motobike == other_motobike)  # True
print(id(my_motobike) == id(other_motobike))

# Получение значений из словаря
print(my_motobike['brand'])

print(my_motobike['price'])

# print(dir(my_motobike))

# Изменение значений в словаре
my_motobike['price'] = 23500
print(my_motobike)

# Добавление элементов в словать
my_motobike['is_new'] = True
my_motobike['delivery'] = True
my_motobike['delivery2'] = True
print(my_motobike)

# Удаление элементов
del my_motobike['delivery2']
print(my_motobike)

# Использование переменных
key_name = 'brand'
my_motobike[key_name] = 'BMW'

print(my_motobike)

# Вложенные словари
my_avto = {
    'brand': 'Hundai',
    'engine_vol': 1.8,
    'price_info': {
        'price': 850000,
        'is_available': True
    }
}

print(my_avto['price_info']['price'])
print(my_avto['price_info']['is_available'])

# Использование переменных для создания словарей
brand = 'Ducati'
bike_price = 25000
engine_volume = 1.2

my_moto = {
    'brand': brand,
    'price': bike_price,
    'engine_vol': engine_volume,
}

print(my_moto)

# Длинна словаря
print(len(my_moto))
print(len(my_motobike))

# Несуществующие ключи и метод get
# print(my_motobike['model'])  # будет ошибка

print(my_motobike.get('model'))

# Задать значение по умолчанию методу GET
print(my_moto.get('delivery', False))
print(my_motobike.get('discont', 0))

# Метод __doc__
my_dict = {}
print(my_dict.__doc__)

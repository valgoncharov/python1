my_list = [True, 10, 'abc', {}]

for elem in my_list:
    print(elem)

my_tuple = ('1920x1080', True, 27)

for elem in my_tuple:
    print(elem)

my_dict = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

for key in my_dict:
    print(key)

for key in my_dict:
    print(key, my_dict[key])

# Example
# List
for el in [1, 'abc', True]:
    print(type(el))
    print(el)

print(el)

print(dir())
# Tuple
for el in (1, 'abc', True):
    print(type(el))
    print(el)
# Dict
for key in {'id': 324}:
    print(type(key))
    print(key)

my_dict = {'id': 324}

for key in my_dict:
    print(my_dict[key])

# Example ITEMS()

my_object = {
    'x': 10,
    'y': True
}

for item in my_object.items():
    key, value = item
    print(key, value)

for key, value in my_object.items():
    print(key, value)

# Example set()

my_name = 'Valentin'

for val in my_name:
    print(val)

# Example RANGE

for num in range(5):
    print(num)

for odd_num in range(3, 10, 2):
    print(odd_num)

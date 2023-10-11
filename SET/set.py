my_fruits = {'apple', 'banana', 'lime'}

posts_ids = {151, 245, 762, 167}

user_inputs = {True, 'hi!', ':-)', 10.5}

print(my_fruits)

print(type(my_fruits))

post_ids = {151, 245, 167, 167, 151}

print(post_ids)

print(type(post_ids))

other_fruits = {'lime', 'apple', 'banana'}

print(my_fruits == other_fruits)

print(len(post_ids))

# Практика
po_ids = {10, 25, 16, 73}

# po_ids[1]  # Ошибка из-за того, что нет магического метода getitem

photo_dimensions = {'1920x1080', '800x600'}
print(len(photo_dimensions))

# del photo_dimensions[1] Удалять с помощью del нельзя

my_set = {10, 10, 5, 15, 15}
print(my_set)
print(len(my_set))

my_set1 = {}

print(my_set1)
print(type(my_set1))

my_set2 = set()  # Вернет пустой набор

print(my_set2)

# Методы наборов
phhoto_sizes = {'1920x1080', '800x600'}

phhoto_sizes.add('1024x768')

print(phhoto_sizes)

other_sizes = {'800x600', '1024x768'}

all_sizes = phhoto_sizes.union(other_sizes)

print(all_sizes)

# Intersections Пересечение наборов
common_s = phhoto_sizes.intersection(other_sizes)
print(common_s)

# Issubset Один набор включен в другой
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}

res = nums.issubset(other_nums)

print(res)  # True

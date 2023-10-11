my_set = {'abc', 'd', 'f', 'y'}

other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.intersection('abc'))
print(my_set.intersection('abcd'))
print(my_set & other_set)

print(my_set.union(other_set))

print(other_set.issubset(my_set))
print(my_set.issubset(other_set))
print(my_set == other_set)

print(my_set.difference(other_set))

print(my_set.discard('d'))  # Удаляет элемент в наборе
print(my_set)

# my_set.remove('def')
# print(my_set) Будет ошибка, так как нет такого элемента

my_set.remove('y')
print(my_set)

copied_set = my_set.copy()

my_set.add('t')
copied_set.add('l')

print(my_set & copied_set)

print(my_set)
print(copied_set)


# Найдем элементы, которые не пересекаются
my_set1 = {'qwe', 'w', 'p', 'o'}

my_set2 = {'tr', 'w', 'o', 'a'}
a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 'l'}
# Пересечения, которых нет во множестве
print(my_set1.symmetric_difference(my_set2))

print((my_set1 | my_set2) - (my_set1 & my_set2))
# Семмитричная разница
print((a | b) - (a & b))

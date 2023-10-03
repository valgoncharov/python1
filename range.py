my_range = range(7)

print(type(my_range))

print(my_range)

print(list(my_range))

my_range1 = range(10, 20, 3)

print(type(my_range1))

print(my_range1)

print(list(my_range1))

print(my_range1[0])
print(my_range1[1])
print(my_range1[2])

for n in my_range1:
    print(n)

my_range2 = range(5)

print(my_range2)
print(type(my_range2))
print(my_range2[-1])

# Создадим цикл
for n in my_range2:
    print(n)

for n in range(5):
    print(n)

# Укажем диапазон
for n in range(2, 7):
    print(n)

for n in range(12, 25, 3):
    print(n)

print(list(range(12, 25, 5)))
print(tuple(range(12, 25, 5)))
print(set(range(12, 25, 5)))
print(dir(my_range2))

print(my_range2.start)
print(my_range2.stop)
print(my_range2.step)

# print(my_range1.index(2))

print(my_range1.count(33))  # Возвращает 0 или 1

# Последовательности: сравнение типов

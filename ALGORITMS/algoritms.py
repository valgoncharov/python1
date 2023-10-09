# Сортировка выборкой

import math
nums = [5, 7, 6, 9, 8, 2, 4, 3, 1]

print("Was", nums)

for i in range(len(nums)):
    lowest = i  # первый элемент примим за наименьший

    for j in range(i+1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j  # нашли элемент меньше в правом срезе

    nums[i], nums[lowest] = nums[lowest], nums[i]


print("Become", nums)

# Линейный поиск
names = ["Володя", "Валера", "Вася", "Саша", "Антон", "Яков"]
search_for = "Антон"  # То что ищем


def linear_search(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]  # Возвращаем индекс

    return None  # или None если не найдено


print("Find element", search_for, "finded by index",
      linear_search(names, search_for))

# Бинарный поиск
nums = [5, 7, 6, 9, 8, 2, 4, 3, 1]
nums.sort()  # сортируем
print(nums)

search_for = 9  # то что ищем

lowest = 0
highest = len(nums) - 1
index = None  # Будущий индекс искомого элемента

while (lowest <= highest) and (index is None):
    # повторяем пока не найдено
    mid = (lowest+highest) // 2  # середина

    if nums[mid] == search_for:
        # нащли по середине
        index = mid
    else:
        if search_for < nums[mid]:
            # Ищем в левой части списка (среза)
            highest = mid - 1
        else:
            # Ищем в правой части списка (среза)
            lowest = mid + 1

print("Find element", search_for, "is by indexs", index)

# Алгоритм Евклида - нахождение НОД


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


print("NOD numbers 30, 18 = ", gcd(30, 18))
# В питоне есь встроенный метод

print(math.gcd(30, 18))


# Переворот строки
some_string = "Howdy Ho!"


def reverse_string(s):
    chars = list(s)  # разбиваем стороку на символы

    for i in range(len(s) // 2):
        # до середины
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp

    return ''.join(chars)


print(some_string)
print(reverse_string(some_string))

# Оператор среза
# Самый быстрый и легкий в Python
print(some_string[::-1])

# Сортировка пузырьком

import math
nums = [2, 5, 1, 8, 7, 3, 4, 6, 9]

print(nums)

for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)

# Вычисление факториал числа
# Первый способ: Рекурсия

number = 5


def factorial(n):
    if n == 0:
        return 1

    return factorial(n-1) * n


print("Factorial numder {n} is {f}".format
      (n=number, f=factorial(number)))

# Второй способ: Цикл
number1 = 100


def factorial_while(n):
    if n == 0:
        return 1

    f = 1
    i = 0

    while i < n:
        i += 1
        f = f * i

    return f


print("Factorial numder {n} is {f}".format
      (n=number1, f=factorial(number1)))


# Числа Фибоначи
# 1 способ

f1 = f2 = 1
n = 12

print(f1, end=' ')
print(f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2  # сумма двух предыдцщих чисел
    print(f2, end=' ')


# Вывод конкретного ряда

f1 = f2 = 1
n = 10

for i in range(2, n):
    f1, f2 = f2, f1 + f2  # сумма двух предыдцщих чисел
    # print(a2, end=' ')

print(f2, end='')

# Математический способ, до 71 элемента


def fib(n):
    golden_ration = (1 + math.sqrt(5)) / 2
    val = (golden_ration**n - (1 - golden_ration))**n / math.sqrt(5)
    return int(round(val))


print(fib(10))

# Решение проблемы выше


def fibb():
    f1, f2 = 0, 1

    while True:
        yield f1
        f1, f2 = f2, f1 + f2


for i, f in zip(range(10+1), fibb()):
    print("{i:3}: {f:3}".format(i=i, f=f))

# Расстояние Левенштейна
str1 = "Привет"
str2 = "Првет"


def dist(a, b):
    def rec(i, j):
        if i == 0 or j == 0:
            # если строка пустаяб то расстояние равняется
            # ее длине (n вставок)
            return max(i, j)
        elif a[i-1] == b[j-1]:
            # если последние символы одинаковые,
            # просто съедаем их
            return rec(i-1, j-1)
        else:
            # иначе считаем минимальный вариант
            return 1 + min(
                rec(i, j-1),  # удаление символа
                rec(i-1, j),  # вставка символа
                rec(i-1, j-1),  # замена символа
            )

    return rec(len(a), len(b))


str1 = "Привет"
str2 = "Првет"

lev = dist(str1, str2)

print("Distance Levenshtein: " + str(lev))

str1 = "Hello"
str2 = "Helo"

lev = dist(str1, str2)
bigger = max([len(str1), len(str2)])
pct = ((bigger - lev) / bigger) * 100


print(
    "String #1 : {str1}\nString #2 : {str2}\n===\nSimilarity : {pct}%".format(
        str1=str1, str2=str2, pct=pct)
)

# Односвязный список


class Node:
    # ячейка списка
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    # односвязный список
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head != None:
            c = self.head
            out = "LinkedList [" + str(c.value)

            while c.next != None:
                c = c.next
                out += ", " + str(c.value)

            out += "]"
            return out
        else:
            return "LinkedList []"

    def add(self, n):
        self.length += 1

        if self.head == None:
            self.head = self.tail = Node(n, None)
        else:
            self.tail.next = self.tail = Node(n, None)

    def reverser(self):
        # разворачивание односвязного списка
        pNode = None
        cNode = self.head
        nNode = cNode.next

        self.tail = cNode

        while nNode != None:
            cNode.next = pNode
            pNode = cNode
            cNode = nNode
            nNode = cNode.next

        cNode.next = pNode
        self.head = cNode


L = LinkedList()

L.add(1)
L.add(2)
L.add(3)

print(L)

L.reverser()

print(L)

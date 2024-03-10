def divide_nums(a, b):
    if b == 0:
        raise TypeError("Second argument can't be 0")
    return a / b


def divide_nums1(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0")
    return a / b


try:
    divide_nums(10, 0)
# т.к. выше мы ловим деление на 0, то этот блок можно убрать
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print('Continue...')

try:
    divide_nums(10, 0)
except TypeError as e:
    print(e)

print('Continue...')

try:
    divide_nums(10, 3)
except TypeError as e:
    print(e)

print('Continue...')


try:
    divide_nums1(10, 0)
except Exception as e:
    print(e)

print('Continue...')

try:
    divide_nums1(10, 0)
except ValueError as e:
    print(e)

print('Continue...')

# try:
#     # Выполнение блока кода
#     pass
# except ErrorType:
#     # Этот блок выполняется в случае возникновения ошибок в блоке try
#     pass

try:
    print(10/0)
except ZeroDivisionError:
    print("Error - Division by zero!")

print('Continue...')

try:
    print(10/5)
except ZeroDivisionError:
    print("Error - Division by zero!")

print('Continue...')


# try:
#     print(10 + '2')  # Не обрабатывает такую ошибку
# except ZeroDivisionError:
#     print("Error - Division by zero!")

# print('Continue...')

try:
    print(10/0)
except ZeroDivisionError:
    print(ZeroDivisionError)
    print("Error - Division by zero!")

print('Continue...')

# Получение информации об ошибке
try:
    print(10/0)
except ZeroDivisionError as e:
    print(type(e))
    # <class 'ZeroDivisionError'>
    print(dir(e))
    print(e)  # division by zero
    print(e.__str__)

print('Continue...')

# Добавление еще одного типа ошибки в обработку
try:
    print('10'/0)
    # TypeError: unsupported operand type(s) for /: 'str' and 'int'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(type(e))
    print(e)
    # unsupported operand type(s) for /: 'str' and 'int'
print('Continue...')

# Block ELSE
try:
    print(10/5)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("There was no error")

print('Continue...')

# Block FINALLY
try:
    print(10/5)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("There was no error")
finally:
    print('Continue...')

# Любые ошибки в блоке Exception
try:
    print(10/0)
except Exception as e:  # здесь будет инфо об ошибке
    print(e)

try:
    print(10/0)
except:  # тут не будет информации об ошибке
    print("Some error occurred")


try:
    print(10/0)
except ZeroDivisionError as e:
    print(isinstance(e, ZeroDivisionError))
    print(e)
except TypeError as e:
    print(e)

print('Continue...')

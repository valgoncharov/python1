# test_file = open('test.txt', 'w')

# print(test_file)
# print(type(test_file))s
# Ниже пример равносилен данному
# test_file.write("First string\n")
# test_file.write("Second string\n")

# test_file.close()

with open('test.txt', 'w') as test_file:
    test_file.write("First string\n")
    test_file.write("Second string\n")
    test_file.write("Third string\n")


# test_file = open('test.txt')

# print(test_file.read())

# test_file.close()

# with open('test.txt') as test_file:
#     for line in test_file:
#         print(line)

# with open('test.txt') as test_file:
#     print(test_file.readline())
#     print(test_file.readline())
#     print(test_file.readline())
#     res = test_file.readline()
#     print(res)
#     print(res == "")
with open('test.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break

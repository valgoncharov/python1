import os


def create_directory(path):
    try:
        os.makedirs(path)
        print(f"Directory '{path}' created successfully")
    except FileExistsError:
        print(f"Directory '{path}' already exists")
    except Exception as e:
        print(f"An error occurred: {e}")


# Пример использования функции:
create_directory("new_folder")


with open('new_folder/test.txt', 'w') as test_file:
    test_file.write("First string\n")
    test_file.write("Second string\n")
    test_file.write("Third string\n")

with open('new_folder/test1.txt', 'w') as test_file:
    test_file.write("First string\n")
    test_file.write("Second string\n")
    test_file.write("Third string\n")

with open('new_folder/test.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break

with open('new_folder/test1.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break
my_file = "new_folder/test.txt"
if my_file.exists():
    my_file.unlink()

my_file1 = "new_folder/test1.txt"
if my_file1.exists():
    my_file1.unlink()

from array import array

my_int_array = array("i", [12, 321, 10])

print(my_int_array)
print(type(my_int_array))

my_int_array.append(15)

print(my_int_array)

# my_int_array.append("122")

print(my_int_array.count(1))
# my_int_array.pop()

print(my_int_array)

print(len(my_int_array))

my_int_array.append(33)

for elem in my_int_array:
    print(elem)

print(my_int_array[2])

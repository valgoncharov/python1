from array import array

my_int_array = array("i", [12, 321, 10, 11, 5, 7])

with open('my_array.bin', 'wb') as myfile:
    my_int_array.tofile(myfile)


imported_array = array('i')

with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)


imported_array.reverse()
print(imported_array)

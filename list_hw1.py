hw_list = [2, True, 'abc', 5.4, 'yes']
hw_list1 = [2, 77, 'abc', 5.4, 99]

all_list = hw_list + hw_list1
all_list1 = hw_list.__add__(hw_list1)

print(all_list)
print(all_list1)

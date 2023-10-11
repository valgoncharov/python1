hw_list = [2, True, 'abc', 5.4, 'yes']
hw_list1 = [2, 77, 'abc', 5.4, 99]

del hw_list[2]
hw_list
del hw_list1[2]
print(hw_list)
print(hw_list1)
print(len(hw_list))

hw_list1.sort()
sort_list1 = hw_list1.sort(reverse=True)
print(hw_list)
print(sort_list1)

new_list = [3, 5]
plus_list = new_list + hw_list
plus_list1 = new_list + hw_list + hw_list1
print(plus_list)
print(help(plus_list))
print(id(plus_list))
print(plus_list1)

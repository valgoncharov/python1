my_dict = {'a': True, 'b': 10, 'c': 'abc'}

del my_dict['a']

my_dict.__delitem__('b')

print(my_dict)

print(my_dict.__delitem__)

# print(del my_dict[0])

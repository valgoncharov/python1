# '10' + 5

# 5 + '10'

5 + int('10')

int_num = 5
float_num = 4.5

# print(int_num + float_num)  # 9.5
print(float_num + int_num)
# magic
print(int_num.__add__(float_num))  # NotImplemented
print(float_num.__radd__(int_num))  # 9.5

bool_val = True
int_val = 7

print(bool_val + int_val)  # 8

print(bool)
print(bool(10))

print(dir(bool))

print(bool.__doc__)

print(str.__doc__)

print(help(list.__eq__))

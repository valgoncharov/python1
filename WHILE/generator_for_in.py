from sys import getsizeof
# nums = (3, 5, 10)

# squares = (num * num for num in nums)

# print(type(squares))

# print(squares)

# squares1 = (num * num for num in range(6))

# print(type(squares1))

# print(squares1)

# for num in squares1:
#     print(num)

# nums1 = [3, 5, 10]
# squares2 = (num * num for num in nums1)

# squares3 = list(squares2)
# print(squares3)
# print(type(squares3))

# nums2 = [3, 5, 10]
# squares3 = (num * num for num in nums2)

# squares4 = tuple(squares3)
# print(squares4)
# print(type(squares4))


# Example
squares_gen = (num * num for num in range(10000))
print(getsizeof(squares_gen))
# 208
print(type(squares_gen))

squares_list = [num * num for num in range(10000)]

print(getsizeof(squares_list))
# 85176
print(type(squares_list))

squares_gen1 = (num * num for num in range(100_000_000))
print(getsizeof(squares_gen1))
# 208
print(type(squares_gen1))

for elem in squares_gen1:
    print(elem)
    if elem == 100:
        break

squares_list1 = [num * num for num in range(100_000_000)]

print(getsizeof(squares_list1))
# 835128600
print(type(squares_list1))

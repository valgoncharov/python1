my_car = {
    'brand': 'Toyta',
    'price': 10_000
}

print('band' in my_car)
print('year' in my_car)
print('year' not in my_car)

print(bool(0))
print(bool(0.0))
print(bool(0j))

print(bool(None))

print(bool({}))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool(range(0)))
print(bool(''))

print(not not {})  # False
print(not not {'a': 10})  # True


my_list = [1, 2]

if len(my_list) > 0:
    print("List has elements")

my_lis = []

print(len(my_lis) > 0)

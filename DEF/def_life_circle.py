def my_fn():
    global a
    a = 10


my_fn()

print(a)

a = 10


def my_f():
    global a
    a = 15


my_f()

print(a)  # 15
# Example
c = 10


def me_fn(a, b):
    print(c)
    print(a, b)


me_fn('abc', 'xyz')

print(a)

print(dir())

a = 5
b = 3
c = a + b
print(c)

a = 8
b = 12
c = a + b
print(c)


def sum(a, b):
    c = a + b
    print(c)


a = 5
b = 3

sum(a, b)

a = 8
b = 12

sum(a, b)
print(type(sum))


def my_fn(a, b):
    a = a + 1
    c = a + b
    return c


res = my_fn(10, 3)
print(res)


def my_fn():
    pass


print(my_fn())


def my_fn1(a, b):
    a = a + 1
    c = a + b
    return c


num_one = 10
num_two = 5

res = my_fn1(num_one, num_two)
print(res)  # В видео 15(?)
print(num_one)


def increase_person_age(person):
    print(id(person))
    person['age'] += 1
    return person


person_one = {
    'name': 'Bob',
    'age': 21
}
print(id(person_one))

increase_person_age(person_one)
print(person_one['age'])

# Создание копии обьекта


def increase_person_age1(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy


person_one1 = {
    'name': 'Bob',
    'age': 21
}
print(id(person_one1))

new_person = increase_person_age1(person_one1)
print(new_person['age'])
print(person_one1['age'])

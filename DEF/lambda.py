def mult(a, b):
    return a * b

# mult = lambda a, b: a * b


print(mult(10, 5))

# Example


def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")

print(morning_greeting('Val'))

evening_greeting = greeting("Good Evening")

print(evening_greeting('Val'))

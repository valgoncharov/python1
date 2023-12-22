button = {
    'width': 200,
    'text': 'Buy'
}

red_button = {
    **button,
    'color': 'red'
}

print(red_button)

print(button)

green_button = {
    'color': 'green',
    **button
}

print(green_button)

two_button = {
    'color': 'blue',
    **red_button
}

print(two_button)

# Обьединение словарей
button_info = {
    'text': 'Buy'
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}

button_unit = {
    **button_info,
    **button_style
}

print(button_unit)

# Обьединение словарей более проще
button_unit1 = button_style | button_info

print(button_unit1)
# Приоритет имеет второй операнд
button_info1 = {
    'color': 'black',
    'wigth': 50
}
button_unit2 = button_style | button_info1
print(button_unit2)

# Обьединение 3х словарей

button_unit3 = {
    **button_info,
    **button_unit1,
    **button_style
}
print(button_unit3)

button_unit4 = button | button_info | button_style
print(button_unit4)

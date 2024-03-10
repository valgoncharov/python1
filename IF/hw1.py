# My
def route_info(dict_1):
    if dict_1.get('distance'):
        return f"Distance to your destination is {dict_1}"
    if dict_1.get('speed') and dict_1.get('time'):
        return f"Distance to your destination is {dict_1['speed'] * dict_1['time']}"

    return f"No distance info is available"


a = {'distance': 100}
print(route_info(a))
b = {'speed': 100, 'time': 2}
print(route_info(b))

print(route_info)


def route_info(info_dict):
    if 'distance' in info_dict and isinstance(info_dict['distance'], int):
        return f"Distance to your destination is {info_dict['distance']}"
    elif 'speed' in info_dict and 'time' in info_dict:
        return f"Distance to your destination is {info_dict['speed'] * info_dict['time']}"
    else:
        return "No distance info is available"


# Пример использования функции:
dictionary1 = {'distance': 50}
print(route_info(dictionary1))  # Вывод: Distance to your destination is 50

dictionary2 = {'speed': 60, 'time': 2}
print(route_info(dictionary2))  # Вывод: Distance to your destination is 120

dictionary3 = {'location': 'City'}
print(route_info(dictionary3))  # Вывод: No distance info is available


# Theacher
def route_info1(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']}"

    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"

    return "No distance info is available"


print(route_info1({'distance': 15}))
print(route_info1({'distance': '15'}))

print(route_info1({'speed': 15, 'time': 3}))

print(route_info1({'my_speed': 15, 'time': 3}))


def route_info2(route):
    if ('distance' in route) and (type(route['distance']) == int):
        route_info2 = f"Distance to your destination is {route['distance']}"
    elif ('speed' in route) and ('time' in route):
        route_info2 = f"Distance to your destination is {route['speed'] * route['time']}"
    else:
        route_info2 = "No distance info is available"
    return route_info2

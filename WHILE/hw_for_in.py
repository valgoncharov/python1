# Task 1
def dict_to_list(dict_to_convert):
    return list(dict_to_convert.items())


def dict_to_list1(dict_to_convert1):
    list_for_convertion = []
    for k, v in dict_to_convert1.items():
        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))
    return list_for_convertion


print(dict_to_list1({'a': True, 'b': [], 'c': 5}))


# Task 2
def filter_list(list_to_filter, value_type):
    filtered_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            filtered_list.append(element)
    return filtered_list


print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))


# Не рекомендуется использовать isinstance
def filter_list1(list_to_filter1, value_type1):
    filtered_list = []
    for element in list_to_filter1:
        if isinstance(element, value_type1):
            filtered_list.append(element)
    return filtered_list


print(filter_list1([35, True, 'abc', 10], int))
print(filter_list1([35, True, 'abc', 10], str))
print(filter_list1([35, True, 'abc', 10], bool))

# Значения логического типа явл экземплярами классов bool, int, object
print(isinstance(True, bool))
print(isinstance(True, int))
print(isinstance(True, object))


# Use filter
def function_filter(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)

    return filter(check_element_type, list_to_filter)


res = function_filter([1, 10, 'abc', 5.5], int)
print(res)  # Будет выведен объект


def function_filter1(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)

    return list(filter(check_element_type, list_to_filter))


res1 = function_filter1([1, 10, 'abc', 5.5], int)
res2 = function_filter1([1, 10, 'abc', 5.5], float)
res3 = function_filter1([1, 10, 'abc', 5.5], str)
res4 = function_filter1([1, 10, 'abc', True, 5.5], int)
print(res1)
print(res2)
print(res3)
print(res4)
# Как проверить, что bool явл подклассом int
print(int.__subclasses__())


def function_filter2(list_to_filter, value_type):
    def check_element_type(elem):
        print(type(elem))
        return type(elem) is value_type

    return list(filter(check_element_type, list_to_filter))


res5 = function_filter2([1, 10, 'abc', True, 5.5], int)
res6 = function_filter2([1, 10, 'abc', 5.5], int)
res7 = function_filter2([1, 10, 'abc', 5.5], float)
res8 = function_filter2([1, 10, 'abc', 5.5], str)
print(res5)
print(res6)
print(res7)
print(res8)


# Exampel use lambda function
def function_filter3(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type,
                       list_to_filter))


res9 = function_filter3([1, 10, 'abc', 5.5], int)
print(res9)

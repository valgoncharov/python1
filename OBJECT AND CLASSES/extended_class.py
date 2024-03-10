class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


class MyExtendedList(ExtendedList):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_list = ExtendedList([3, 5, 2])

custom_list.print_list_info()

custom_list.append(7)
custom_list.print_list_info()

print(custom_list.__dict__)

# print(ExtendedList.__dict__)
print(ExtendedList.__subclasses__())
# print(list.__dict__)
print(list.__subclasses__())
# print(object.__dict__)

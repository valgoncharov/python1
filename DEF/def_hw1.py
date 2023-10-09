def merge_lists_to_dict7(as1, be):
    c = zip(as1, be)
    d = dict(c)
    return d


info = merge_lists_to_dict7(as1='name', be='Val')
info1 = merge_lists_to_dict7('name', be='Bob')
print(info)
print(info1)


def update_car_info():
    car = dict
    return car

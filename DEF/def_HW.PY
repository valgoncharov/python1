def merge_lists_to_dict(a, b):
    c = zip(a, b)
    d = dict(c)
    return d


a1 = ['apple', 'banana', 'lime']
b1 = [100, 70, 50]
res = merge_lists_to_dict(a1, b1)
print(res)


def merge_lists_to_dict1(a, b):
    c = zip(a, b)
    d = dict(c)
    return d


a1 = ['apple', 'banana', 'lime']
b1 = [100, 70, 50]
res = merge_lists_to_dict1(a1, b1)
print(res)
a = reversed()


def merge_lists_to_dict7(as1, be):
    c = zip(as1, be)
    d = dict(c)
    return d


info = merge_lists_to_dict7(as1=2, be='Val')
print(info)

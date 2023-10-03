def sum_nums(a, b):
    c = a + b
    return (c)


print(sum_nums(2, 5))
# print(sum_nums(2))
# print(sum_nums())
# print(sum_nums(3, 1, 3))


def sum_num(*args):
    print(args)
    print(type(args))

    print(args[0])
    return sum(args)


print(sum_num(2, 3, 7))


def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info('Val', 40)
print(info)

# Аргументы с ключевыми словами


def get_posts_info1(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info(posts_qty=40, name='Val')
print(info)


def get_posts_info2(**person):
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote"
        f"{person['posts_qty']} posts"
    )
    return info


info = get_posts_info2(posts_qty=40, name='Val')
print(info)


def get_posts_info3(**person):
    print(person)
    print(type(person))
    info1 = f"{person['name']} wrote {person.get('posts_qty')} posts"
    return info1


info1 = get_posts_info3(posts_num=40, name='Val')
print(info1)


#
def get_posts_info4(**person):
    print(person)
    print(type(person))
    info2 = f"{person['name']} wrote {person['posts_qty']} posts"
    return info2


info2 = get_posts_info4(posts_qty=40, name='Val', id=675)
print(info2)

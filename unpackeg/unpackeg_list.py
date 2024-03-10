user_data = ['Val', 23]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"


# Произойдет распаковка позиционных аргумента
# Но, аргументов должно быть 2
print(user_info(*user_data))
# print(user_info(user_data)) - oшибка будет
print(user_info(user_data[0], user_data[1]))
print(user_info(name=user_data[0], comments_qty=user_data[1]))

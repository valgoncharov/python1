def other_fn():
    # Some actions...
    pass


def fn_with_callback(callback_fn):
    callback_fn()


fn_with_callback(other_fn)

# Example


def print_num_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def print_square_num(num):
    print("Square of the num is", num * num)


def process_num(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Enter any number: '))

process_num(entered_num, print_num_info)
process_num(entered_num, print_square_num)

# Example


def send_data(data):
    # sending data to the remote server
    pass


def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    # actions with updated_data
    send_data_fn(updated_data)


process_data({'name': 'Val'}, send_data)
print(process_data)

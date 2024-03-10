my_num = 21.5

print("is int") if type(my_num) is int else print("is not int")

if type(my_num) is int:
    print("is int")
else:
    print("is not int")

# Example

# send_img(img) if img.get['is_processed'] else process_and_send_img(img)

# Example

product_qty = 10

print("in stock" if product_qty > 0 else "out of stock")

temp = +24

weather = "hot" if temp > 18 else "cold"
print(weather)

# Example

my_img = ('1920', '1080')

# info = (f"{my_img[0]}x{my_img[1]}") if len(
#     my_img) == 2 else print("Incorrect image formatting")
# print(info)

if len(my_img) == 2:
    my_hw = f"{my_img[0]}x{my_img[1]}"
else:
    my_hw = "Incorrect image formatting"

print(my_hw)

my_str = 'This is'
my_str1 = 'How you doing?'

my_str2 = (f"String is long") if len(
    my_str1) > 10 else print("String is short")
print(my_str2)

print("String is long" if len(
    my_str1) > 10 else "String is short")

if len(my_str) > 10:
    print("String is long")
else:
    print("String is short")

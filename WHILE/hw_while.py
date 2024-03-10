# My solution
# def hw_while():
#     """This is function about division two numbers"""
# while True:
#     num1 = int(input("Set the first number: "))
#     num2 = int(input("Set the second number: "))
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError:
#         print("Error - Division by zero!")
#     answer = input("Enter yes or no: ")
#     if answer == 'no':
#         break
#     else:
#         answer == 'yes'
#         continue


# Solution
while True:
    try:
        num_one = float(input("Please enter number one: "))
        num_two = float(input("Please enter number two: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue
    try:
        print(num_one / num_two)
    except ZeroDivisionError as e:
        print(e)
        print("Error - Division by zero!")

    answer = input("Do you want to continue? (yes/no): ")
    if answer == 'no':
        break
    else:
        answer == 'yes'
        continue

import random
i = 10

while i < 50:
    print(i)
    i += 10

# Infinite loop
# while True:
#     print("Infinite loop")

# Break loop
while True:
    answer = input("Enter yes or no: ")
    if answer == 'no':
        break


random_num = random.randint(1, 5)
while True:
    num = int(input("Guess the number from 1 to 5: "))
    if num != random_num:
        print("Try again...")
        continue
    print("Congratulations!", random_num)
    break

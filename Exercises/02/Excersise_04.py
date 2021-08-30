#b) Add a menu for choosing difficulty level of the game
#c) Feel free to extend this program with features of your choice.
# a)

import random as rnd
import time

# a)
"""
n = 0
while n < 2:
    x = rnd.randint(1,10)
    y = rnd.randint(1,10)

    print(f"{x} * {y}")
    answer = int(input("Enter your answer = "))

    if (x*y) == answer:
        print(f"Your are correct {x} * {y} = {answer}")
    else:
        print(" Incorrect answer")
    n += 1
"""
# b) Add a menu for choosing difficulty level of the game
# not ok yet

n = 0
def choices():

    print("1: Want a faster level in multiplication?")
    print("2: Want to try addition?")
    print("3: Want to try subtraction?")


x = rnd.randint(1, 10)
y = rnd.randint(1, 10)

while True:
    try:
        choice = int(input("Enter the number for your choice: "))

        if choice == 1:

            start = time.time()
            answer = int(input(f"{x} * {y} = "))
            end = time.time()
            elapsed_time = end - start

            if (x*y) == answer and elapsed_time <= 2:
                print(f"Your are correct {x} * {y} = {answer}")
                continue
            elif (x*y) != answer and elapsed_time <= 2:
                print("Wrong answer! ")
            else:
                print("To long time")
            choices()

        elif choice == 2:
            answer = int(input(f"{x} + {y} = "))

            if (x + y) == answer:
                print(f"Your are correct {x} + {y} = {answer}")
            else:
                print(" Incorrect answer")
                break
            n += 1

        elif choice == 3:
            answer = int(input(f"{x} - {y} = "))

            if (x - y) == answer:
                print(f"Your are correct {x} - {y} = {answer}")
            else:
                print(" Incorrect answer")
                break
            n += 1
    except:
        print("Invalid input")

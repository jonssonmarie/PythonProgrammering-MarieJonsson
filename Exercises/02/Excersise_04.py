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

# time in sec
level_time = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

print("Welcome to multiplication game!")
print("Choose a level, 1 - 5, were 1 is the fastest")

# loop to check right answer and time
while True:
    x = rnd.randint(1, 10)
    y = rnd.randint(1, 10)
    try:
        choice = int(input("Enter the number for your choice: "))

        start = time.time()
        answer = int(input(f"{x} * {y} = "))
        end = time.time()
        elapsed_time = end - start

        for i, j in level_time.items():
            n = level_time[i]
            if n == choice:
                slot = level_time[j]

        if (x*y) == answer:
            if elapsed_time <= slot:
                print(f"Your are correct {x} * {y} = {answer}")
                continue
            else:
                print("To long time")
                print("Elapsed  time = ", elapsed_time)
                break
                
        elif (x*y) != answer and elapsed_time <= slot:
            print("Wrong answer! ")
            print("Right answer are", x * y)
            break
            
        elif (x*y) != answer and elapsed_time > slot:
            print("To long time")
            break
            
    except:
        print("Invalid input")


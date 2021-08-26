# a) Create a guessing number game following this flow chart:

import random as rnd
import sys

num = rnd.randint(1, 100)
guess = 13

num_loop = 0
hint = " "


while num_loop < 10:

    guess = int(input("Enter a integer between 1 and 100: "))
    if guess == num:
        print(" Congratulations, yoy won! ")
    if num > guess and num_loop < 10:
        hint = "higher number"
        num_loop += 1
    if num < guess and num_loop < 10:
        hint = "lower number"
        num_loop += 1
    if num_loop == 9:
        print("End of game!")
        sys.exit(0)

    print(f"Enter a new number. A hint choose a {hint}!")



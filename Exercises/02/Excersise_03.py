# Guess number game (*)
# a) Create a guessing number game following this flow chart:

import random as rnd

n = 0

while n < 10:
    rand_num = rnd.randint(1, 100)
    guess = int(input("Guess the number the computer gives, 1 - 100 : "))
    if rand_num == guess:
        print(" Correct")
    elif rand_num < guess:
        print("Guess a lower number")
    elif rand_num > guess:
        print("Guess a higher number")
    n += 1

   
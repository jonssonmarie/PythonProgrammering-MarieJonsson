# Guess number game (*)
# a) Create a guessing number game following this flow chart:
# b) Make an algorithm to automatically guess the correct number. 
#    Can you optimize to get as few guesses as possible?

import random as rnd
"""
n = 0

while n < 10:
    rand_num = rnd.randint(1, 100)
    guess = int(input("Give a number for the computer to guess, 1 - 100 : "))
    if rand_num == guess:
        print(" Correct")
    elif rand_num < guess:
        print("Guess a lower number")
    elif rand_num > guess:
        print("Guess a higher number")
    n += 1
"""
# b) - ej fintrimmad

low = 1
high = 100
i = 0

user_num = int(input("Give a number for the computer to guess, 1 - 100: "))
comp_guess = rnd.randint(low, high)

while comp_guess != user_num :
    if comp_guess > user_num:
        high = comp_guess - 1
        comp_guess = rnd.randint(low, high)
    else:
        low = comp_guess + 1
        comp_guess = rnd.randint(low, high)
    i +=1
    print("No of loops:", i)
    print("The computer takes a guess...", user_num, comp_guess)
    print(f"Correct guess: {comp_guess} = {user_num}")


"""
Guess the number
The computer thinks of a four-digit number. 
Start by creating a random four-digit number. 
Use for statement to figure out a correct guess
"""
"""
Guess the number
The computer thinks of a four-digit number.
Start by creating a random four-digit number.
Use for statement to figure out a correct guess
"""

import random as rnd

four_digit_no = rnd.randint(1000,10000)
low = 1000
high = 10000

for i in range(100):
    comp = ((high+low)//2)
    if comp > four_digit_no:
        high = comp
    elif comp < four_digit_no:
        low = comp + 1
    else:
        print(f"Correct guess is performed since {comp} = {four_digit_no}")
        break

print(f"Correct at Loop {i}, {comp} = {four_digit_no}")

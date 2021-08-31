"""
Guess the number
The computer thinks of a four-digit number. 
Start by creating a random four-digit number. 
Use for statement to figure out a correct guess
"""
import random as rnd


comp = rnd.randint(1000, 10000)
four_digit_no = int(input("Enter a four digit number between 1000 and 9999: "))

low = 1000
high = 10000
i = 0

for i in range(100):
    if comp > four_digit_no:
        high = comp
        comp = rnd.randint(low, high)
    elif comp < four_digit_no:
        low = comp + 1
        comp = rnd.randint(low, high)
    else:
        print(f"Correct guess is performed since {comp} = {four_digit_no}")
        break
    i += 1

print()
print(f"Correct at Loop {i},  {comp} = {four_digit_no}")

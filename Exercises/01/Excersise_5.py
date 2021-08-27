"""
Divisible
Let the user input a number. Check if the number is
- even or odd
- is divisible by 5
- is divisble by 5 and odd
"""


num = int(input("Enter a integer: "))

if num % 2 != 0:
    print("Number is odd")
else:
    print("Number is even")

if num % 5 == 0:
    print("Number is divisable with 5")

if num % 2 != 0 and num % 5 == 0:
    print("Number is divisable with 5 and odd")
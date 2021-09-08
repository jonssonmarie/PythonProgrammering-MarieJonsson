"""
Change
Create a function that takes a value as input parameter and print out 
the banknotes and coins in Swedish currency representing this value. 
For example 5289 would give the following printout:

5st 1000-lapp
1st 200-lapp
1st 50-lapp
1st 20-lapp
1st 10-krona
1st 5-krona
2st 2-krona
Now let the user input a value, and use the function to calculate the change.

Jag tog bort lite och lade till valörer som stämmer med dagens
"""

# en annat alternativ på lösning

def calculate_change(value):
    banknotes = [1000, 500, 200, 100, 20, 10, 2, 1, 0.50]

    for i in banknotes:
        num = value // i
        value = value - (num * i)
        if num > 0:
            print(f"{num:.0f} of {i}-notes")


value = float(input("Enter a value: "))

print("The return of change is :")
calculate_change(value)


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

Jag lade med lite fler valörer
"""
def money_change(value):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # need to have the same number of numbers as banknotes to be able to zip.
                                               # used to temporary save the counts
    banknotes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50]
    for i, count in zip(banknotes, count):
        if value >= i:
            count = value // i
            value = value - i * count
            print(f" {i} : {count:.0f} number of banknotes")


value = float(input("Enter a value: "))
money_change(value)

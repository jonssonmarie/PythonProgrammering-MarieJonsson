# Medicin
# The information in the following table is stated in a medicine package.
# Let the user input an age and a weight, the program should recommend
# the number of pills for the user.
"""
                                  Age          Number of pills
Adults & adolescent over 40 kg    over 12 y     1-2
Children 26-40 kg                  7-12 y       1/2 -1
Children 15-25 kg                  3-7 y        1/2
"""
# vikt viktigare än ålder

age = int(input("Enter the users age: "))
weight = float(input("Enter the users weight: "))

if weight >= 26 and weight <= 40:
    if age >= 7 and age <= 12:
        print(" Number of pills: 1/2 - 1 ")
    else:
        print("Check with doctor since weight and age is not according to medicine package")

elif weight > 40:
    if age > 12:
        print(" Number of pills: 1 - 2 ")
    else:
        print("Check with doctor since weight and age is not according to medicine package")

elif weight >= 15 and weight <26:
    if age >= 3 and age < 8:
        print(" Number of pills: 1/2 ")
    else:
        print("Check with doctor since weight and age is not according to medicine package")

else:
    print("To low weight or age! Medicine is not allowed ")
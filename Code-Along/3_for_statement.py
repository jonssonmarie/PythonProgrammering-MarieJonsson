# for loop with statements
# for each loop, alltså för varje x i listan går den igenom
# exemple i Python på for loop
# for i in range(10):
#   print(i)
#
"""
for i in range(10):
   print(i, end =" ")

print()

# every third number
for i in range(1,20,3):
    print(i,  end = " ")

print(f"\n{range(10)}")
print(f"En lista från range(10): {list(range(10))}")    

# sum all numbers between 0 - 5

sum_ = 0     # sum is a inbuilt func in Python. Do not use as variabel!

for i in range(6):
    sum_ += i
    if i == 5:
        continue
    print(f"{i}", end= " ")
    

print(f"{i} = {sum_}") 
print(sum(range(6)))

import random as rnd
num_six, dice_rolls = 0, 10000
# count number of six
for i in range(dice_rolls):
    dice = rnd.randint(1,6)
    if dice == 6:
        num_six += 1
print(f"Number of six: {num_six} in {dice_rolls} dice_rolls")
print(f"Probability of six: {100*(num_six/dice_rolls):.3f} %")
print("Theoreticla propability", 100*(1/6), "%")

fruits = ["apple", "orange", "strawberry", "grape"]

print("I love to eat: ")

for fruit in fruits:
    print(fruit)


print("Shopping list:")

for i, fruit in enumerate(fruits):
    print(f"{i}.{fruit}")

"""
#############################
# nationella prov uppg - pastauppgift Ma3C

import math
import matplotlib.pyplot as plt

# math.exp(1)  # hur man skrive upphöjt e

# MA3C HT14 uppg 18
"""
t = (2021-1960)
print(t)
for year in range(t):
    pasta_consumtion = 0.791 * math.exp(0.0526*year)
    if pasta_consumtion >= 15:
        print(f"År {year + 1960} är pasta konsumtionen 15 kg")
        break
print(pasta_consumtion)
"""
pasta_per_year = []
t = (2021-1960)

for year in range(t):
    pasta_consumtion = 0.791 * math.exp(0.0526*year)
    pasta_per_year.append(pasta_consumtion)



plt.plot(pasta_per_year)
plt.ylabel("Pastakonsumtion i kg")
plt.title("Pastakonsumtion per kg person från 1960")
plt.show()


""" 
# Nested loops
for row in range(0,3):
    for col in range(0,3):
        print(f"({row},{col})", end= " ")
    print() """
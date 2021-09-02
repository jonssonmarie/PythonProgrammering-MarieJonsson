"""
Dice rolls convergence
Simulate:
  a) 100 dice rolls and count the number of outcome six.
  b) 10, 100, 1000, 10000, 100000, 1000000 dice rolls. 
     Count the number of outcome six in each simulation and store it in a list. 
     Compute the probability of outcome six in each simulation. 
  c)   Use matplotlib to plot this list. 
"""

import random as rnd
import matplotlib.pyplot as plt

# a) hur många sexor blir det på 100 kast med tärningen
""" 
dices = []
i = 0

for i in range(100):
    dice = rnd.randint(1,100)
    dices.append(dice)

print(dices)
print(dices.count(6))

# alternative count
num = 6
j = 0
for elem in dices:
    if elem == num:
        j += 1

print(j) """

# b) count how many sixes from each run, get the propabilty

lst_dice_rolls = [10, 100, 1000, 10000, 100000, 1000000]

num_sixes = []
lst_prop = []

for el in lst_dice_rolls:
    num_dices = []
    for m in range(el):
        dice = rnd.randint(1,6)
        num_dices.append(dice)
    num_six = num_dices.count(6)
    six_prop = (num_six/el)
    num_sixes.append(num_six)
    lst_prop.append(six_prop)

print(f"Number of sixes for each simulation: {num_sixes}")
print(f"Propability for each simulation: {lst_prop}")


# c) 
# plot of number of sixes for each simuation
plt.plot(num_sixes)
plt.ylabel("Number of sixes for each simulation")
plt.title("Number of sixes")
plt.show()

# plot of propability for each simuation
plt.plot(lst_prop)
plt.ylabel("Propability of sixes for each simulation")
plt.title("Propability of sixes")
plt.show()
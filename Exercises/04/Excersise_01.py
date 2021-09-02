"""
Dice rolls
Simulate 10 dice rolls and append the rolls to a list or use list comprehension.

  a)   sort the list in ascending order
  b)   sort the list in descending order
  c)   find the maximum and minimum value in the list
"""

import random as rnd

# a) ascending order

# Alternativ a
dices = []

for dice in range(10):
  dice = rnd.randint(1,6)
  dices.append(dice)
dices.sort()
print(f"Ascending order: {dices}")

# Alternativ b, snabbare än Alternativ a
dices2 = [rnd.randint(1,6) for dice in range(10)]
dices2.sort()
print(f"Ascending order: {dices2}")

# b) descending order

dices3 = [rnd.randint(1,6) for dice in range(10)]
dices3.sort(reverse=True)
print(f"Decending order: {dices3}")

# c) maximum and minimum value
dices4 = [rnd.randint(1,6) for dice in range(10)]

min_value = min(dices4)
max_value = max(dices4)
print(f"dices4: {dices4}")
print(f"Min value: {min_value}, Max value: {max_value}")
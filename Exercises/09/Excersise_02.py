"""
Dice simulation 
Simulate 1000000 dice rolls and save the number of 
ones, twos, ..., sixes in a dictionary. 
Then print them out in the terminal.
"""

import random as rnd

dices = {}
# simulerar tärningskast
for i in range(0,1000000):
    dice = rnd.randint(1,6)
    dices[i] = dice

# räknar antal per 1-6 genom att göra dict till list och sedan använda count
print("No 1:",list(dices.values()).count(1))
print("No 2:",list(dices.values()).count(2))
print("No 3:",list(dices.values()).count(3))
print("No 4:",list(dices.values()).count(4))
print("No 5:",list(dices.values()).count(5))
print("No 6:",list(dices.values()).count(6))


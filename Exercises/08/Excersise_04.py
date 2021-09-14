"""
Dice roll experiment
Simulate 10, 100, 1000, 10000, 100000 dice rolls and count the freqencies 
and probabilities for each number in each simulation. 
Create a new text file using Python with the name "simulation.txt" 
and write the results to that text file.

Frequency = Frekvensen motsvarar antalet svar av de olika observationsvärdena. 
P = antal gynnsamma utfall/ antal möjliga utfall
"""

import random as rnd

path = "../files/simulation.txt"
  
num = [10, 100, 1000, 10000, 100000]

with open(path, "w+") as f1:
    
    for x in num:
        dice_rolls = []
        for i in range(0,x):
            dice = rnd.randint(1,6)
            dice_rolls.append(dice)
        f1.write(f"Number of rolls: {x}   \n")

        for j in range(1,7):
            count_outcome = dice_rolls.count(j)
            p = count_outcome/x      
            f1.write(f"{j} : {count_outcome}, propability {p:.3f}\n")
        f1.write(f"\n")
       
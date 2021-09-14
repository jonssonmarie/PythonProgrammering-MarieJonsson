"""
Dice roll experiment
Simulate 10, 100, 1000, 10000, 100000 dice rolls and count the freqencies 
and probabilities for each number in each simulation. 
Create a new text file using Python with the name "simulation.txt" 
and write the results to that text file.

P(event) = (number of outcomes in the event / number of outcomes in the sample space)
Frequency = Frekvensen (den absoluta frekvensen) motsvarar antalet svar 
(förekomster) av de olika observationsvärdena. 
"""

import random as rnd

dice_roll = []
path = "Files/simulation.txt"


def dice_rolls(num):
    pass

def frecuency_dice(dice_roll):
    for i in range(1,6):
        count_outcome = dice_roll.count(i)

        p = count_outcome/6
        print("frequency: ",count_outcome, i)
        print(f"propability: {p:.2f}")
    return count_outcome, p
   
num = [10, 100, 1000, 10000, 100000]

with open(path, "w+") as f1:
    for x in num:
        for i in range(0,x):
            dice = rnd.randint(1,6)
            dice_roll.append(dice)

        for i in range(1,6):
            count_outcome = dice_roll.count(i)
            p = count_outcome/6
            print("frequency: ",count_outcome, i)
            print(f"propability: {p:.2f}")


        f1.write(f"Number of rolls: {num}")
        f1.write(count_outcome, p)

    pass



dice_rolls(10)
print(dice_roll)
frecuency_dice(dice_roll)


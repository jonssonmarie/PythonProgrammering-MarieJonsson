"""
Dice rolls
Create a textfile called dice_rolls.txt using Python. 
Also for each subtask, write adequate headers.
  a) Simulate 20 dice rolls and write them to your textfile.
  b) Sort the dice rolls from a) and write them to a separate row in the 
     same textfile.
  c) Count the number of fours in the dice rolls and write them to a 
     separate row in the same textfile.
"""
import random as rnd


with open("Files/dice_rolls.txt", "w") as f1:
    dice_rolls =[rnd.randint(1,6) for i in range(0,20)] # a)
    print("innan sort()", dice_rolls)
    dice_rolls.sort()               #b) sorting 1 - 6
    
    count_4 = dice_rolls.count(4)   # c) count the numbers of 4
    f1.write(f"Sorted list: {dice_rolls}\n")  # write to separate row
    f1.write(f"Number of fours: {count_4}")   # write to separate row



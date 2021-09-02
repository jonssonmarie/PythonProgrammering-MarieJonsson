"""
Schema
9.00 - 11.45
  - stand up
         - studieteknik jag använder
  - listor
    - acces
    - slicing
    - change items
    - add items

  - kl 11 Sofia kommer och tar startpuls + klassråd



13.15 -16.00
  - stuga

 word_len = [len(word) for word in words if word != "the"]

[gör detta för x i denna om x != något]
"""

# access items - operator []
tv_shows = ["Antikrundan","Mästerkockarna", "Aktuellt", "Talang"," Äta"]

print(f"tv_shows[0]: {tv_shows[0]}")
print(f"tv_shows[-1]: {tv_shows[-1]}")

# slicing operator - operator :
print(f"tv_shows-:]: {tv_shows[:]}")
print(f"tv_shows[1:]: {tv_shows[1:]}")
print(f"tv_shows[1:3]: {tv_shows[1:3]}")  # notera start till end-1, i detta fall tas 3 ej med
print(f"tv_shows[::-1]: {tv_shows[::-1]}") # [start: end-1: step]


# change list items
tv_shows[0] = "Vetenskapens Värld"
print(tv_shows)

# add items
tv_shows.append("Go kväll")
print(tv_shows)

# iterate through list

for tv_show in tv_shows:
    print(tv_show)

print("Tv tablå")
for tv_show in enumerate(tv_shows):
    print(f"{i}: {tv_show}")

# add items to a list - lsit of cubes

cubes = []

for i in range(10):
    cubes.append(i**3)

print(cubes)

# list comprehension
cubes2 = [x**3 for x in range(10)]
cubes3 = [x**3 for x in range(10) if x != 3]
print(cubes2)
print(cubes3)

import random as rnd

dices = [rnd.randint(1,6) for _ in range(10)]
print(dices)
dices.sort() # return nones
print(dices)
tv_shows = ["Antikrundan","Mästerkockarna", "Aktuellt", "Talang","Äta", "89"]
tv_shows.sort() # sort works for one datatype at the time
print(tv_shows)
tv_shows.sort(reverse=True)
print(tv_shows)

# sub lists, lista i lista

grades = [["A", 30],["B", 25],["C", 20]]
print(f"grades[1][0]: Betyg: {grades[1][0]}")


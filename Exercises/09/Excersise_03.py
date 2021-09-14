"""
Pokemon list
Read in the file pokemon_list.txt in Python. 
Create a variable with name pokedex with the 
key:value "pokemon":"type, index". 
For example when searching for the keys "Gengar" and "Pikachu":
print(pokedex["Gengar"])
print(pokedex["Pikachu"])
 
Spöke/Gift, 94
Elektrisk, 25
"""

path = "../files/pokemon_list.txt"

fi = path.read()
print(fi)
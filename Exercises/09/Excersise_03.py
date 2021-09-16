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

pokedex = {} # "pokemon": "type, index"

# öppnar fil och rensar data, ssplitar och lägger ihop och lägger i en dictionary
with open(path, "r", encoding ="utf-8") as f1:
    datan = f1.readlines()
    #print(datan)
    
    for data in datan:
        d = data.strip(" \n")
        d_split = d.split(" ")
        val = d_split[2], d_split[0]
        val_set = ", ".join(val)
        pokedex[d_split[1]] = val_set
        
# printar en sökning i dict och returnerar value            
print(pokedex["Dragonair"])
print(pokedex["Dragonite"])
print(pokedex["Pikachu"])

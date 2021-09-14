"""
Morse code
Read in the file morse.txt, save it in a dictionary and create a 
function that lets the user input a message to get it translated to morse code. 
For example

print(morse["SOS"])
print(morse["POKEMON"])
 
...---...
.------.-.------.

"""
path = "../files/morse.txt"
with open(path, "r", encoding= "utf-8") as f1:
    data = f1.readlines()

    print(data)
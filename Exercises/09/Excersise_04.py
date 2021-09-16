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

morse = {}
sentence = input("Skriv in en mening eller ord du vill ha översatt till morse: ")

# ändrar till stor bokstav, söker igenom och hittar rätt morse kod per bokstav i meningen
def morse_code(sentence, morse):
    sentence_morse = " "
    for char in sentence:
        if char.isalpha():
            if char != " ":
                char = char.upper()
                sentence_morse += morse[char] + " "  # dict[key] returnernar value
            elif not char.isalpha():
                sentence_morse += ""
            else:
                sentence_morse += " "
    print(f"Översättning till Morse: {sentence_morse}")

# öppnar filen, rensar och flyttar till en dictionary
with open(path, "r", encoding= "utf-8") as f1:
    datan = f1.readlines()

    for data in datan:
        data_cleaned = data.strip("\n")
        data_split = data_cleaned.split(" ")
        for data in data_split:
            key = data[0:1]
            morse[key] = data_split[1]

    morse_code(sentence, morse)

    
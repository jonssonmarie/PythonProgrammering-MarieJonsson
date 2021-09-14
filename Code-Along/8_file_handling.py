"""
9:00 - 11:45
filhantering 
ledningsgrupp på besök kl 15:00
labben ska in nästa fredag (v38)
torsdag -> labb

Stuga
Kokchun repeterar for, list, strängar, funktioner?
annars jobba med exercises
"""
"""
options:
r -read
w - write
a - append
x - create file
"""

# "with" tar hand om felhanteringen och stänger filen som öppnats
# use this when opening files, takes car eof error handling and close the file

"""with open("Files/quotes.txt",'r') as f:  # "r" option stands for read file
    text = f.read()

print(text)
"""


# clean up quotes.txt
"""
- inspect file text
- removeing leading and trailing whitespaces
- remove excessive whitespaces between words
- remove /n

- add quote numbers
- exctract authors 
"""

import re

path = "Files/quotes.txt"
path_clean = "Files/quotes_clean.txt"

"""
with open(path, "r") as f1, open (path_clean, "w") as f2:
    #.readlines()  # ger en lista med flera strings
    i = 1
    f2.write("Famous Quotes\n")  # skriver till f2

    for quote in f1.readlines():
        quote = quote.strip(" \n") #mellanslaget innan \n tar bort leading och trailing mellanslag
        quote = re.sub(" +", " ", quote)  # + säger ett eller flera
        #print(repr(quote))
        
        if quote != "":
            f2.write(f"{i}.{quote}\n")  # skriver och ger radbyte och numrering
            i+=1

"""

"""
Extract authors from quote_clean.txt
"""

with open(path_clean, "r") as f1, open(path_clean, "a") as f2:
    #print(f1.read())
    quotes = [quote.strip(" \n") for quote in f1.readlines() if quote[0].isdigit()]
    #print(quotes)
    authors = [quote.split()[-2:] for quote in quotes]
    authors =set([" ".join(author) for author in authors]) # set gives unique

    print(authors)

    f2.write( "\nAuthors: ")

    for author in authors:
        f2.write(f"{author}, ")



firstname = "Kokchun"
lastname= "Giang"

# concatenating strings

fullname =  firstname + " " + lastname

school = "IT-högskolan"
adress = "Ebbe Liberathsgatan 18C"
phone = "112"

print(fullname)

# Multilining f-string
contact_details = f"""
Name: {fullname}
School: {school}
Adress: {adress}
Phone: {phone}
"""

print(contact_details)


# Concatenate with looop

bamba = "Chili sin Carne, köttbullar, Fisk, Pannkakor, Taco".split(", ")  # (, ) har mellanslag för att få jämn kant då Chili sin ej har mellanslag först
bamba
# ett sätt att splitta en string spearerad med tex kommatecken - använd split
days = "Må Ti On To Fr".split()
days

menu= "Veckomeny\n"

for day, food in zip(days, bamba):  # day får varje element i days, food får varje element i bamba
    menu += f"{day}: {food}\n"
print(menu)

# Indexing
#  - indeing with [] operator to access elements
# - slicing operator:

quote = "!False - it's funny because it's True"  # " " fungerar,  ' ' fungerar inte
# quote = '!False - it's funny because it's True'  ' '  fungerar inte då de ävne finns i ord
# quote = '!False - its funny because its True'  ' '  fungerar om ej ' i text
print(quote)
print (f"quote[0] : {quote[0]}")
print (f"quote[-1] : {quote[-1]}")
print (f"quote[-4:] : {quote[-4:]}")
print (f"quote[1:6] : {quote[1:6]}")  #  [start:stop-1]
print (f"Backwords quote[::-1] : {quote[::-1]}")  #  [start:stop-1]


# Split strings another way
#numbers =input("Ange några tal separerade med  mellanslag: ").split() 
# data type is string, split returnerar lista av strängar

#numbers = [float(number) for number in numbers if number.isdigit()]
####  look for another method
#print(numbers)

#mean = sum(numbers/len(numbers))
#print(f" Medelvärder är {mean}")

# Regular expression
# - find particular patterns in a string
#  - e.g phone numbers, perosnal numbers, emails

import re

text = "Mitt telefonnummer är 031-123456, Adas telefonsnummer är 032-456789 och Bedas: 033-987543"

match1 = re.findall(r"\d\d\d-\d\d\d\d\d\d", text)  # ett sätt
match2 = re.findall(r"\d{3}-\d{6}", text)  # ett annat sätt
print(match1)
print(match2)


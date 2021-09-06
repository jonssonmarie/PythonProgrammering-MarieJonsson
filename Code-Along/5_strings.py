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
numbers = input("Ange några tal separerade med  mellanslag: ").split()  # data type is string
print(numbers)  # split leverear en lista [] av strängar





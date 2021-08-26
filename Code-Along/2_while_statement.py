# skriva alla tal mellan -10 och 10

""" n = -10

while n <= 10:
    print (n, end = ", ")
    n += 1 """


# skriva ut alla jämna tal mellan -10 och 10

""" while n <= 10: 
    if n % 2 == 0:
        print(n, end = ", ")
        n += 2  """

""" while n <= 10:
    print(n, end = ", ")
    n += 2 """


# shift alt a ger kommentarar bort det markerade styket, bortkommenterar med samma snabbkommande


# summera alla udda tal mellan 0 och 10
""" n = 1
summa = 0
while n <= 10:
    if n == 9:
        print("9 =", end = " ")
    else:
        print(f"{n} +", end = " ")
    summa += n
    n += 2

print(summa)
 """

"""
Fåglar och oljeutsläpp
- finns 8000 fåglar från början
- ett oljeutsläpp gör att populationen halveras varje år
- hur många år tar det tills populationen blivit en tiondel?
"""

""" birds, year = 8000, 0

while birds >= 800:
    birds /= 2
    year += 1
    print(f"År {year}: antal {birds:.0f} st")
    # good enough även om år inte räknas ut i denna visning
 """
"""
Mjölkuppgift
 - 1l mjölk 1 500 000 bakterier i rumstemperatur
 - Antalet bakterier ökar med 50% per timme i rumstemperatur
 -  Mjölk surnar när vi har med än 10 000 000 st bakterier
"""

""" bact, hour = 1500000, 0

while bact <= 10000000:
    bact *= 1.5
    hour += 1
    print(f"Mjölken är sur inom {hour}") 

 """

import matplotlib.pyplot as plt

faktor= 1.5 
bakterier = 1.5e6
bakterie_lista = []
sur = 1e7
timmar =0

while bakterier < sur:
    bakterie_lista.append(bakterier)
    bakterier *= faktor
    timmar += 1
print(f"Det tar {timmar}h för mjölken att surna")
print(bakterie_lista)
plt.plot(bakterie_lista)
#plt.plot(range(0, timmar+1), bakterie_lista, "o-")
#plt.plot(range(0,timmar+1), [sur]*(timmar+1))

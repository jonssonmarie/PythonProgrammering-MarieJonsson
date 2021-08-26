"""
IG: 0 - 10
G: 11 -20
VG: 21- 30
MVG: > 30
"""
import random as rnd

points = rnd.randint(0,35)   # slumpat heltal mellan 0 och 35
print(points)

if points > 30:
    print("MVG")
elif points > 20:
    print("VG")
elif points > 10:
    print("G")
else:
    print("IG")

number = 10
if number % 2 == 0 and number % 5 == 0:
    print("jämnt och delbar med 5")

if number % 2 == 0:
    if number % 5 == 0:
        print("Jämt och delbar med 5")


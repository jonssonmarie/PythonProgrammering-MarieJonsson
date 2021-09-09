"""
Dagens schema:
9-11.45 Föreläsning
    - ledningsgruppmöte 21 sept
        - visualiseringskurs byts ut mot linjär algebra - Kokchun
    - felhantering
    - 
13.15- 16.00 Stuga
    - jobba själv
    - repetera gammalt

LAB 2 fredag v38  är deadline    
"""


# Error types
# avmarkera för test          prin("hej")

# a practice of reading error messages


"""
ovanstående ger detta svar:
NameError med vilken rad mm
"""
"""
- syntax error - Python parser don't aunderstand the code
- logical errors - hard dot find - gives unpredictable results
- exceptions - Python parser know what to do, but can't do it
"""


# logical error
"""
import math
print(math.pi)

area_circle = lambda radius: 2*math.pi*radius

print(area_circle(10))
"""
# hard to find logical error Area for a circle is 2pi*r^2. 
# Omkrets = 2pi*r

# exception errors

"""


numbers = list(range(10)) # index 10 doesn't exist in this list which ends at 9
print(numbers)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(numbers[10])


print("hej")
namn = input("Vad heter du?: ")
#   print = namn  # farligt print har blivit ett variabelnamn 
#   och skriver över functionen print
print(namn)  # är den rätt syntaxen
"""


# ett annat vanligt fel är import tex plotlib och samtidigt har en fil som heter som modulen
# plotlib.py


#age = int(input("Hur gammal är du? "))  
# användaren kan skriva in skumma saker    
#print(f"Du är {age} gammal")


# Try - except

"""
Try block  - testa farlig kod som kan krascha
Except block  - 
Raise
"""


"""
age = (input("Hur gammal är du? "))  # ger en sträng i return

try :
    age = float(age)
    if not 0 <= age <= 125:
        raise ValueError(f"Ålderns ka vara mellan 0 och 125 inte {age}")

except ValueError as err:
    print(err)

print("Programmet fortsätter här")
"""

"""
# Loop while True
while True:
    age = (input("Hur gammal är du? "))  

    try :
        age = float(age)
        if not 0 <= age <= 125:
            raise ValueError(f"Ålderns ka vara mellan 0 och 125 inte {age}")
        break
    except ValueError as err:
        print(err)

print(f"Du är {age} år gammal")

"""

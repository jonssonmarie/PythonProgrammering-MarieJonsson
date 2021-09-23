"""
Polymorphism
same function name or operator used for different types
e.g. len() on a string, len() on a list
plus operator + on a string concatenates the string while on an int performs integer addition
"""

"""
Polymorphism
same function name or operator used for different types
e.g. len() on a string, len() on a list
plus operator + on a string concatenates the string while on an int performs integer addition
"""
"""
print(f"len(['a','b','c']): {len(['a','b','c'])}")
print(f"len('abc'): {len('abc')}")
"""

# Polymorfish in class methods

class Fish:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am a fish, my name is {self.name}"

    def speak(self):
        print("Blupp blupp")


class Fox:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am a fox, my name is {self.name}, no one knows how I sound"

    def speak(self):
        return NotImplemented # as we don't know the sound of the fox 


animals = (Fish("Pelle"), Fox("Ylvis"))

# although animals have different types, you can iterate through it and call same method as they are bound to different objects
for animal in animals:
    print(animal)
    animal.speak()
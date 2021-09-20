"""
9.00 -11.45 Föreläsning
labb2 - in på fredag
OOP - ObjectOrienterad Programmering

13.15 - 16.00 Stuga

Formulär:
    Det här tycker jag är intressant

    Intressant: programmering

    Svårt: Minnas

class()
create a class using the class keyword
an object is instantiated from the class using the constructor
__init__() - "dunder init" is an initializer method which is called when the object is created
used for setting initial values of attributes, which are variables associated with an object
if not specified, Python will call a default __init__()
methods - functions bound to the class
self - when a method of an object is called, the object itself is passed into the self parameter
all methods have a self parameter
"""


"""
class Antagning:            # creates a class
    def __init__(self):     
        pass


a1 = Antagning()      # instanciated an object from the class Antagningen
print(a1)
"""



""" 
class Antagning(): 
    # self reference to the object that is created
    def __init__(self, school, program, name, accept =  False):     # None # dunder init
        # for methiods (and functions) Positional parameters först, sist default arguments
         # assign the arguments to object attributes
        self.school = school
        self.program = program
        self.name = name
        self.accept = accept

    def __repr__(self) -> str:
        return f"Antagning(school='{self.school}',program='{self.program}', name='{self.name}', accept={self.accept})"
       
person1 = Antagning("cool school", "AI", "Gore Bord", False)  # Constructor
person2 = Antagning("IT-skola", "UX", name = "Gorat Borat")
print(person1.name)
print(person1.school)
print(person1.accept)
print(person1.__dict__)  # dunder dict
print(person2.accept)
print(person2.name)

print(person2)
 """


class OldCoinsStash:
    def __init__(self, owner):
        self.owner = owner

        # these attributes are "private" - only allow to access them in the class
        self._riksdaler = 0
        self._skilling = 0

    def deposit(self, riksdaler: float = 0, skilling: float = 0) -> None:
        if riksdaler <= 0 or skilling <= 0:
            raise ValueError(
                f"You try to deposit {riksdaler} riksdaler and {skilling} skilling. They have to be positive")

        self._riksdaler += riksdaler
        self._skilling += skilling

    def withdraw(self, riksdaler: float, skilling: float):
        if riksdaler > self._riksdaler or skilling > self._skilling:
            raise ValueError(
                f"You can't withdraw more than you have in your stash")

        self._riksdaler -= riksdaler
        self._skilling -= skilling


    def check_balance(self) -> str:
        return f"Coins in stash: {self._riksdaler} riksdaler, {self._skilling} skilling"

    def __repr__(self) -> str:
        return f"OldCoinStash(owner='{self.owner}')"

# manuel testing
stash1 = OldCoinsStash("Gore Bord")
print(stash1) # testing __repr__
print(stash1.check_balance())    # glöm inte () bakom parametern för att få anropet
stash1.deposit(riksdaler = 500, skilling = 3000)
print(stash1.check_balance())

try:
    stash1.deposit(-10,35)
except ValueError as err:
    print(err)

print(stash1.withdraw(100,100)) # testing withdraw
print(stash1.check_balance())

try:
    stash1.withdraw(1000,35000)
except ValueError as err:
    print(err)

print(stash1.check_balance())

# försk att råna denna stashen :)

stash1._riksdaler = 1000000
print(stash1.check_balance())

class Student:
    def __init__(self, name: str, age: float) -> None:
        self.name = name  
        self.age = age  # note no underscore
 
        # property

    @property  
    def age(self) -> float:
        return self._age        # note underscore
        # property och underscore gör att man kan läsa av age men inte 
        # ändra hur som helst men en setter kan ändra det


    @age.setter
    def age(self, value: float) -> None:
        if not isinstance(value, (int,float)):
            raise TypeError(f"Age must be a int or a float not {type(value)}")

        if not (0 <= value < 125):
            raise ValueError(f"Your age must be between 0  and 125")
        
        self._age = value

student1 = Student("Gore Bord", 25)
print(student1.name)
print(student1.age)

try:
    student1.age = "25"
except TypeError as err:
    print(err)
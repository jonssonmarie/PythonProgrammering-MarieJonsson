"""
Inheritance and composition
- methods, properties and attributes from parent class can be accessed from child class using super()
- inheritance has stronger coupled between classes and the relation: "is a", e.g. a Student is a Person
- when changing in the parent class, it might affect the subclasses
- when using inheritance, make sure that the relationship really is an "is a" relation and not a "has a"
- composition has weaker coupling between classes and the relation: "has a", e.g. a Classroom has a Student
"""

import re 

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.age = age 
        self.name = name 

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Age must be int or float not {type(value)}")
        self._age = value    

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if re.search(r"^[A-Ö][-a-öA-Ö]+(\s[A-Ö][-a-öA-Ö]+)?$", value.strip()) is None:
            raise ValueError(f"The value {value} is not a valid name")
        
        self._name = value

    def say_hi(self) -> None:
        print(f"Person {self.name} says hi")

class Student(Person):
    """A Student is a Person that knows a language"""
    def __init__(self, name: str, age: int, language: str) -> None:
        super().__init__(name, age) # self is automatically sent in through super()   # super gör att self fås från Person
        self.language = language


    # overrides say_hi() in Person class
    def say_hi(self) -> None:
        print(f"Student {self.name} knows {self.language}")

class Viking(Person):
    """A Viking has an OldCoinsStash but is a Person"""
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.stash = oldcoins.OldCoinsStash(name)

p1 = Person("Örjan ", 55)
s1 = Student("Åke Olofsson", 25, "Python")
v1 = Viking("Ragnar Lothbroke", 50)

print(v1.stash)
print(v1.stash.check_balance())

people = (p1, s1, v1)

# polymorphic 
for person in people:
    person.say_hi()
    
# note that the Viking does not have a say_hi() method and thus the parents say_hi() is called
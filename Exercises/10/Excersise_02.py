"""
Person
Create a class named Person, with parameterized constructor with the 
following parameters:

name
age
email
Turn name, age, email into properties with following validations in 
their setters:

name - must be string
age - must be number between 0 and 125
email - must include an @ sign
It should also have __repr__ method to represent the Person class 
in a neat way.

Also create a method say_hello() that prints

Hi, my name is ..., I am ... years old, my email address is ...  
"""
"""
Person
Create a class named Person, with parameterized constructor with the
following parameters:

name
age
email
Turn name, age, email into properties with following validations in
their setters:

name - must be string
age - must be number between 0 and 125
email - must include an @ sign
It should also have __repr__ method to represent the Person class
in a neat way.

Also create a method say_hello() that prints

Hi, my name is ..., I am ... years old, my email address is ...
"""
import re

class Person:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def say_hello(self):
        return f"Hi, my name is {self.name}, I am {self.age} years old, my email address is {self.email}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = Person.validate_str(value)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = Person.validate_number(value)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = Person.validate_email(value)

    @staticmethod
    def validate_str(value):
        if not isinstance(value, str):
            raise TypeError(f"Enter a string")
        return value

    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Age must be a int or float not {type(value)}")
        return value

    @staticmethod
    def validate_email(value):
        if re.findall("@", value):
            return value
        else:
            raise TypeError(f"{type(value)} is not valid as email, xxxx@yyyy.zzz is the correct format\n")


    def __repr__(self):
        return f"name:{self.name}, \nage: {self.age} \nemail:{self.email}\n"


try:
    beata = Person("Beata34", 56, "beata_karlsson@banjo.com")
except TypeError as err:
    print(err)
except NameError as err:
    print(err)

anna = Person("Anna", 68, "anna_andersson@himlen.se")

print(f"Persons hallo:  {anna.say_hello()}\n")
print(f"Persons name: {anna.name}")
print(f"Persons age:  {anna.age}")
print(f"Persons email:  {anna.email}")


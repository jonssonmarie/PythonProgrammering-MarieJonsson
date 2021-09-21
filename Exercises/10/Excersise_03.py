"""
Student and Teacher 
Create two classes named Student and Teacher that inherits from Person.

The Student class shall have:
study() method that prints out

study...study...study...more study
override say_hello() with the following message:

Yo, I am a student, my name is ..., I am ... years old, my email address is ...  
The Teacher class shall have:

teach() method that prints out
teach...teach...teach...more teaching
Instantiate a Teacher object and a Student object. Call

teach() and say_hello() methods from your Teacher object.
study() and say_hello() methods from your Student object.
"""
#  INTE KLAR 

import re

class Person:
    def __init__(self, name, age, email, workplace):
        self.name = name
        self.age = age
        self.email = email
        self.workplace = workplace

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception(f"Please use string and not{type(value)}")
        self._name = value


    @property
    def age(self) -> float:
        return self._age

    @age.setter
    def age(self, value) -> float:
        if not isinstance(value, (int, float)):
            raise Exception(f"Please use int or float and not {type(value)}")
        self._age = value
        return value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value) -> str:
        if re.findall("@", value):
            self._email = value
        else:
            raise TypeError(f"{type(value)} is not valid as email, xxxx@yyyy.zzz is the correct format\n")


class Student(Person):
    def study(self):
        return f"study...study...study...more study\n"

    def say_hello(self,):
        return f"Yo, I am a student, my name is {self.name}, I am {self.age} years old, my email address is {self.email}\n"


class Teacher(Student):
    def teach(self):
        return f"teach...teach...teach...more teaching"

    def say_hello(self):
        return f"Yo, I am a teacher my name is {self.name}, I am {self.age} years old, my email address is {self.email} and I work at {self.workplace}\n"
        #return Student.say_hello(self)


student1 = Student("Maggan", 23, "maggan@student.se", "")
print(student1.study())
print("Student class: ",student1.say_hello())

teacher1 = Teacher("Gudrun", 51, "gudrun@teacher.com", "ITHS")
print("Teacher class:",teacher1.say_hello())


student2 = Student("Petra", 25, "petra@student.se", "")
print("Student name:",student2.name)

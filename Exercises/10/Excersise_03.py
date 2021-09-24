"""
Student and Teacher
Create two classes named Student and Teacher that inherits from Person.

The Student class shall have:
 - study() method that prints out: "study...study...study...more study"

 override say_hello() with the following message: Yo, I am a student, my name is ..., I am ... years old, my email address is ...

The Teacher class shall have:
 - teach() method that prints out: teach...teach...teach...more teaching

Instantiate a Teacher object and a Student object.

Call
teach() and say_hello() methods from your Teacher object.
study() and say_hello() methods from your Student object.
"""

import re


class Person:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

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

    def say_hello(self) -> str:
        print(f"Mu name is {self.name}, and I am {self.age} years old, you can reach me at: {self.email}")


class Student(Person):
    def __init__(self, name: str, age: int, email: str, program: str):
        super().__init__(name, age, email)  # self is automatically sent in through super()
        self.program = program

    def study(self) -> str:
        print(f"study...study...study...more study")

    def say_hello(self) -> str:
        print(f"Yo, I am a student, my name is {self.name}, I am {self.age} years old, my email address is: {self.email}\n")


class Teacher(Person):
    def __init__(self, name: str, age: int, email: str, workplace: str, program: str) -> None:
        super().__init__(name, age, email)   # ta in de instanse variabler (tex self.age) du vill över till class Person här. self behövs inte för den kommer automatiskt
        self.workplace = workplace
        self.program = program

    def teach(self) -> str:
        print(f"teach...teach...teach...more teaching")

    def say_hello(self) -> str:
        # override say_hello in Person class since say_hello exist in this class
        print(f"I am a teacher, my name is {self.name}, I am {self.age} years old, I teach in {self.program} my email address is {self.email} and I work at {self.workplace}\n")
        # return Student.say_hello(self)


student1 = Student("Maggan", 23, "maggan@student.se", "Data Science")
student2 = Student("Ove", 25, "ove@student.se", "")
teacher1 = Teacher("Gudrun", 51, "gudrun@teacher.com", "ITHS", "Data Science")
teacher2 = Teacher("Petra", 30, "petra@teacher.com", "GU", "Data Science")


people = [student1, student2, teacher1, teacher2]

# polymorphic
for person in people:
    person.say_hello()
for person in people[:2]:
    person.study()
for person in people[2:]:
    person.teach()


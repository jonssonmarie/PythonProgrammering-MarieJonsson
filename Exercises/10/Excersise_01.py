"""
Unit conversion
Create a class for converting US units to the metric system. 
It should have the following bound methods:

__init__ (self, value)
inch_to_cm(self)             1 inch = 2.54 cm
foot_to_meters(self)            1 m =  3.28 feet
pound_to_kg(self)               1 pound = 0.453592 kg mer säkert: x pounds/ 2.2046 = kg

__repr__(self)
Make sure that value is the correct type and format, 
raise suitable exceptions in case it isn't. 
Make value into property with getter and setter. 
Test your class manually by instantiating an object from it 
and test different methods.
"""
"""
class Person:
    def __init__(self, name, age, height) -> None:
        self.name = name 
        self.age = age
        self.height = height

    @property
    def age(self):
        return self._name

    @age.setter
    def age(self, value):
        self._age = Person.validate_number(value) 

    @property
    def height(self):
        return self._age

    @height.setter
    def height(self, value):
        self._height = Person.validate_number(value)

    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Ange en int eller float inte {type(value)}")

try:
    p1 = Person("Gore", "55", 155)
except TypeError as err:
    print(err)
"""

class UnitConversion:
    def __init__(self, inch_to_cm: float, foot_to_meter: float, pound_to_kg: float):
        self.inch_to_cm = inch_to_cm
        self.foot_to_meter = foot_to_meter
        self.pound_to_kg = pound_to_kg


    @property
    def inch_to_cm(self) -> float:
        return self._inch_to_cm * 2.54

    @inch_to_cm.setter
    def inch_to_cm(self, value):
        self._inch_to_cm = UnitConversion.validate_number(value)


    @property
    def foot_to_meter(self) -> float:
        return self._foot_to_meter / 3.28

    @foot_to_meter.setter
    def foot_to_meter(self, value):
        self._foot_to_meter = UnitConversion.validate_number(value)


    @property
    def pound_to_kg(self):
        return self._pound_to_kg / 2.2046

    @pound_to_kg.setter
    def pound_to_kg(self, value):
        self._pound_to_kg = UnitConversion.validate_number(value)



    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Ange en int eller en float inte {type(value)}")
        return value


    def __repr__(self) -> str:
        return f"UnitConversion(inch_to_cm='{self.inch_to_cm}', foot_to_meter='{self.foot_to_meter}, pound_to_kg='{self.pound_to_kg}')"

convert1 = UnitConversion(2, 3.4, 5)


print(f"inch in meter : {convert1.inch_to_cm:.3f}")
print(f"foot in meter: {convert1.foot_to_meter:.3f}")
print(f"pound in kg: {convert1.pound_to_kg:.3f}")
print(convert1)  # här visas __repr__ och denna visar var alla self argumenten har för värde


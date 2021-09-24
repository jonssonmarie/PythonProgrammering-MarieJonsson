"""
Fraction
Create a class called Frac to represent mathematical fractions.
The class is instantiated with two instance variables: nominator and denominator.
Objects instantiated from this class should have methods for
addition, subtraction, multiplication, division using the operators +,-,*,/.
Note that these implemented methods must be mathematically correct.
Also implement the following methods:

simplify(self, value = None) # simplifies to most simple form unless value is given
__str__(self) # represent the fraction in a neat way for printing
mixed(self) # represent the fraction in mixed terms
__eq__(self, other) # checks equality by overloading ==


Also remember to handle errors and validations.

Example of tests that it should handled:
1/2 + 1/3 = 5/6   ok
1/2 - 1/3 = 1/6   ok
7/6 --> 1 1/6 (mixed)   ok
3*1/2 = 3/2   ok
1/2 * 3 = 3/2  ok
1/4 + 2 = 9/4  ok
1/4 / 1/2 = 1/2  ok
2/4 == 1/2 --> True ok
3/4 += 2 = 11/4 ok
"""
from fractions import Fraction


class Frac:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
        self.simplify(nominator, denominator)

    # return lowest term
    def simplify(self, nominator, denominator):
        while nominator % denominator != 0:
            old_denom = nominator
            old_nom = denominator

            nominator = old_nom
            denominator = old_denom % old_nom
        return denominator

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            new_nom = self.nominator + other * self.denominator
            new_denom = self.denominator
        else:
            if self.validate(self):
                new_nom = self.nominator * other.denominator + other.nominator * self.denominator
                new_denom = self.denominator * other.denominator
        lowest_terms = self.simplify(new_nom, new_denom)
        return Frac(new_nom // lowest_terms, new_denom // lowest_terms )

    def __radd__(self, other):
        # eg. __radd__, __rmul__, __rsub__ function are only called if the left operand does not support the corresponding operation
        print("__radd__ is called ...")
        return self + other

    def __iadd__(self, other):
        print("__iadd__ is called ...")
        if self.validate(self):
            self.nominator += (other * self.denominator)
        return self

    def __sub__(self, other):
        # Return a - b, for a and b numbers.
        if type(other) == int or type(other) == float:
            new_nom = self.nominator - other * self.denominator
            new_denom = self.denominator
        else:
            if self.validate(self):
                new_nom = self.nominator * other.denominator - other.nominator * self.denominator
                new_denom = self.denominator * other.denominator
        lowest_terms = self.simplify(new_nom, new_denom)
        return Frac(new_nom // lowest_terms, new_denom // lowest_terms)

    def __neg__(self):
        # unary negation
        return -1*self

    def __rsub__(self, other):
        print("__rsub__ is called ...")
        return -(self - other)

    def __mul__(self, value):
        # Return a/b * c, for a, b and c numbers.
        if self.validate(self):
            new_nom = self.nominator * value
            return Frac(new_nom , self.denominator)

    def __rmul__(self, value):
        print("__rmul__ is called ...")
        return self * value

    def __truediv__(self, other):
        # return a / b.
        if self.validate(other):
            new_nom = (self.nominator * other.denominator)
            new_denom = self.denominator * other.nominator
            lowest_terms = self.simplify(new_nom, new_denom)
            return Frac(new_nom // lowest_terms, new_denom // lowest_terms)

    def mixed(self, other):
        # represent the fraction in mixed terms
        if self.validate(self):
            rest = self.nominator/self.denominator - self.nominator//self.denominator
            fraction_rest = Fraction(rest)
            return (f"mixed result: {self.nominator//self.denominator} {fraction_rest}")

    @staticmethod
    def validate(value):
        """ validates if two vectors have same length """
        if not isinstance(value.nominator, (int, float)) and not isinstance(value.denominator, (int, float)):
            raise TypeError(f"Age must be a int or float not {type(value.nominator)}, {type(value.denominator)}")
        return value

    def __str__(self):
        # represent the fraction in a neat way for printing
        return f"{self.nominator}/{self.denominator}"

    def __eq__(self, other):
        # checks equality by overloading ==
        if isinstance(other, Frac):
            if other.nominator == self.nominator and other.denominator == self.nominator:
                return True
            return False



# Fractions object
f1 = Frac(5, 2)
f2 = Frac(3, 4)

# add
f3 = f1 + f2
print(f"{f1} + {f2} = {f3}")

f8 = f1 + 3
print(f"{f1} + 3 = {f8}")

f10 = 3 + f1
print(f"3 + {f1} = {f10}")

f22 = f2 + 1
print(f"{f2} + 1 = {f22}")

# sub
f4 = f1 - f2
print(f"{f1} - {f2} = {f4}")

f11 = f1 - 3
print(f"{f1} - 3 = {f11}")

f12 = 3 - f2
print(f"3 - {f2} = {f12}")

# multiplication
f5 = f1 * 3
print(f"{f1} * 3 = {f5}")

f7 = 3 * f1
print(f"3 * {f1} = {f7}")

# division
f6 = f1/f2
print(f"{f1} / {f2} = {f6}")

# mixed terms
print(f"{f1} / {f2} as {f1.mixed(f2)}")

# eq
print(f"{f1} == {f2} : {f1 == f2}")

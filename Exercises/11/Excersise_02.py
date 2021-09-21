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
1/2 + 1/3 = 5/6
1/2 - 1/3 = 1/6
7/6 --> 1 1/6 (mixed)
3*1/2 = 3/2
1/2 * 3 = 3/2
1/4 + 2 = 9/4
1/4 / 1/2 = 1/2
2/4 == 1/2 --> True
3/4 += 2 = 11/4
"""

class Frac:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def addition(self):
        return sum(self.nominator, self.denominator)

    def subtraction(self):
        return abs(self.nominator - self.denominator)

    def multiplication(self):
        return self.nominator * self.denominator

    def division(self):
        return self.nominator/self.denominator

    def simplify(self):
        pass

    def mixed(self):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass
"""
Creating a function - def
def name(param1, param2, ...): 
    statements
    ...

name(arg1, arg2, ...)

"""
def squarer(x): # input parameter x 
    return x**2 # returns x**2

print(squarer(3))
squares = [squarer(x) for x in range(10)]
print(squares)

# Default value
# this function returns None but prints out
def say_hello(name = "friend"):
    print(f"Hi {name}") 

say_hello("Ada")
say_hello() # since no argument is sent - name is assigned the default value "friend"
print(say_hello("Beda")) #it returns None after the statements have executed


def smallest(number1, number2):
    if number1 > number2:
        return number2
    else:
        return number1

print(smallest(3,5))


# Keyword arguments
# - key = value syntax

def count_words(text):
    words = text.split() # assuming a word ends with space
    return len(words)

quote = "I stand on the shoulders of giants"
print(count_words(text = quote)) # used keyword arguments to call this function

"""
Arbitrary arguments, *args
will receive a tuple of arguments, which can be accessed
use * before parameter name e.g.
def func_name(*args):
  statements
  ....
"""

# Draw lines

import matplotlib.pyplot as plt

def draw_lines(x, k=1, m=1, title=""):
    y = [k*x_+ m for x_ in x]

    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)

    x = list(range(-5,5))

x = list(range(-5,5))
draw_lines(x, title="Lines")
draw_lines(x, k=-2, m=1,title="Lines")


#Draw circle

import numpy as np  
import matplotlib.pyplot as plt 

def draw_circle(radius = 1, center = (0,0)):
    x = np.linspace(0, 2*np.pi)
    plt.plot(radius*np.sin(x)+center[0], radius*np.cos(x)+center[1])
    plt.plot(center[0], center[1], '*r')
    plt.axis("equal")

draw_circle()
draw_circle(radius=10,center=(2,2))


"""
Lambda functions
an anonymous function
can take many arguments but have one expression
can be used inside another function
"""

squarer = lambda x: x**2
print(squarer(5))


def n_power(n):
    return lambda x: x**n

third_power = n_power(3)
print(third_power(2))


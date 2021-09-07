"""
Mathematical functions
Make the following functions with def or lambda and plot their
graphs in the same figure window, with x ∈[−10,10]:

  a) f(x)=x**2 − 3
  b) g(x)=4x − 7

What could the relation between  f(x)  and  g(x)  be?
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10) # Return evenly spaced numbers over a specified interval (start,stop)

# a) 
def func_x(x):
    y1 = x**2 - 3
    return y1

# b)
def func_g(x):
    y2 = 4*x -7
    return y2
    
plt.plot(x, y1, x, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("g(x)")
plt.show() 

""" 
deriverar man g(x) fås 4
deriverar man f(x) fås 2x 
i punkten x = 2 har f'(x) och g'(x) samma y värde och lutningen är gemensam där
vilket också PQ formeln konfirmerar
"""


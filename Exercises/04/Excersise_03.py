"""
Squares
  a) Use list comprehension to create a list of squares from -10 to 10
  a) Plot this list using matplotlib. 
"""

import matplotlib.pyplot as plt

# a) list of squares
print([i**2 for i in range(-10,11)])

# b) Plot
squares = [i**2 for i in range(-10,11)]
plt.plot(squares)
plt.ylabel("Squaress")
plt.xlabel("Floats")
plt.title("Squares")
plt.show()

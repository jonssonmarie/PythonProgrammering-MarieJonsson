# Task
# The Euclideam distance between the points P_1 and P_2 
# is the length of a line between them. 
# Let P_1: (3,5) and P_2: (-2,4) and compute the distance between them.

# formula for distance d = sqrt((x2-x1)^2 + (y2-y1)^2)

import math

x2 = -2
x1 = 3
y2 = 4
y1 = 3
# calcutate distance with formula
d = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
print(f"distance is {d:.2f}")

# Alternative solution 
p_1 = [3,5]
p_2 = [-2,4]
# calcutate distance with formula
d = math.sqrt(math.pow((p_2[1]-p_1[1]),2) + math.pow((p_2[0]-p_1[0]),2))
print(f"distance is {d:.2f}")
# Calculate the distance between the points P_1: (2,1,4) and P_2: (3,1,0)
# formula for distance d = sqrt ((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)

import math

p_1 = [2,1, 4]
p_2 = [3,1, 0]

# calcutate distance with formula
dist = math.sqrt(math.pow((p_2[1]-p_1[1]),2) + math.pow((p_2[0]-p_1[0]),2) + math.pow((p_2[2]-p_1[2]),2))

print(f"distance is {dist}")

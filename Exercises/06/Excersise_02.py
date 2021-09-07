"""
Euclidean distance
The formula for Euclidean distance in 2D between P: (p_1, p_2) and Q: (q_1, q_2) is:

d(P,Q) = sqrt((p_1-q_1)^2 + (p_2-q_2)^2)

  a) Create a function that takes two points as input parameters and 
     return the Euclidean between them.
  b) Let the user input two points. Call the function using the users input points. 
  c) Use your function to calculate distances between the origin (0, 0) 
     and each of these points: (10, 3), (-1, -9), (10, -10), (4, -2), (9, -10). 
"""
import math

# a)

# return euclidiaen distans between two points
def euclidiaen_distance(p1, p2):
    distance = math.sqrt(math.pow((p1[0] - p2[0]),2) + math.pow((p1[1]-p2[1]),2))
    return distance

print("a): ", euclidiaen_distance((1,2),(2,3)))
"""
# b)
# user input
first_points = input("Enter a first point x y with whitespace in between : ")
second_points= input("Enter a second point x y with whitespace in between : ")

# from str to int
first_point = [int(i) for i in first_points.strip().split()]
second_point = [int(j) for j in second_points.strip().split()]

print(f"b) 1:st The Euclidean distance is: {euclidiaen_distance(first_point, second_point):1f}")


# Alternativt sätt för b) med map som typecastar variablerna simultant
p1, p2 = map(int,input("Enter a first point x y").split())
q1, q2 = map(int, input("Enter a second point x y").split())

print(f"b 2nd: The Euclidean distance is: {euclidiaen_distance((p1,p2),(q1,q2)):.1f}")
"""
# c)
tuple_points = ((10, 3), (-1, -9), (10, -10), (4, -2), (9, -10))

# from tuple to list
points = []

for x,y in tuple_points:
    p = [x,y]
    points.append(p)

# loop function call
for p in points:
    print(f"Euclidean Distance: {euclidiaen_distance((0,0),(p[0],p[1])):.1f}")
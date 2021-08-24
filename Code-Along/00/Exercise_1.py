import math

# a  
a = 3
b = 4

# calculate the hypotenuse
hyp = (a**2 + b**2)**0.5
print(f"c= {hyp}")

# Alternative solution for a
# calculate the hypotenuse
hyp2 = math.sqrt(math.pow(a,2) +math.pow(b,2))
print(f"c= {hyp2}")


# b

c = 7.0
a = 5.0

# calculate b in the triangle
b = math.sqrt(math.pow(c,2) - math.pow(a,2))
print(f"b = {b:.1f}")
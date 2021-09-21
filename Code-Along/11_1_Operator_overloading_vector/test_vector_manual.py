import vector as vec  # import fil namn as förkortning

""" v1 = vec.Vector(1,2)

print(v1.numbers)
 """

v2 = vec.Vector(1,2,3,4)
v3 = vec.Vector(True, False, 3)
#print(v3.numbers)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

v3 = v1 + v2

print(f"v3 = v1 +v2 = {v3}")
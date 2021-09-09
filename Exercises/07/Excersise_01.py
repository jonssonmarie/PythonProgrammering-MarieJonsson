"""
Find errors
Find the errors in this code to compute the distance between the point (x,y) 
and the origin in a cartesian coordinate system.

impor numpy as np

def distance(x,y)
    reurn np.sqrt(x+y)

print(distance([0.5, 0.5]))
"""

"""
Svar: 
rad 6:  import saknar t
rad 8:  saknar : efter (x,y)
rad 9:  return saknar t 
        samt raden ger roten ur och inte distance mellan två punkter d = sqrt((x1-x2)^2 + (y1-y2)^2)
        där x1,y1 är (0,0)
rad 11: input till funkionen är 1 variabel och funk kräver två variabler. 
        ändra från list till tuple då man bara vill ha en punkt

Fixad:
import numpy as np

def distance(x,y):
    return np.sqrt((0-x)**2 + (0-y)**2)

print(distance(0.5, 0.5))

"""
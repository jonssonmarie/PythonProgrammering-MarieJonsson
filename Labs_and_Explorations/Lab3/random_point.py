# Create random x, y, z
# limits -10, 10 is just for testing script

import random as rnd


def random_point():
    point_x = rnd.randint(-10, 10)
    point_y = rnd.randint(-10, 10)
    point_z = rnd.randint(-10, 10)

    return point_x, point_y, point_z
    
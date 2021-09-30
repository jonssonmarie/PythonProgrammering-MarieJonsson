# Create random x, y, z

import random as rnd


def random_coordinates():
    coord_x = rnd.randint(-5, 10)
    coord_y = rnd.randint(-5, 10)
    coord_z = rnd.randint(-10,10)

    return coord_x, coord_y, coord_z
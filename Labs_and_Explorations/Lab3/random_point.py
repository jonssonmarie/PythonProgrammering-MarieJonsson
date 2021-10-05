# Create random x, y, z
# limits -10, 10 is just for testing script
# high jack bye using # random_point() and add your own points eg. 1,2,3

import random as rnd


def random_point():
    """
    create random x, y, z for a point
    :return: random point x,y,z
    """
    point_x = rnd.randint(-10, 10)
    point_y = rnd.randint(-10, 10)
    point_z = rnd.randint(-10, 10)

    return point_x, point_y, point_z

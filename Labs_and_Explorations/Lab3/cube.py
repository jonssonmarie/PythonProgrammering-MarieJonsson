import matplotlib.pyplot as plt
import numpy as np
import math

from rectangle import Rectangle

from random_point import random_point
point_x, point_y, point_z = random_point()  # high jack in random_point() to set your own coordinates


class Cube(Rectangle):
    """
    A class to create a geometric cube

           Attributes
           ----------
           side1 : float
               side of the cube
           x : float
               cube start point in x direction
           y : float
               cube start point in y direction
           z: float
                cube start point in z direction

           Methods
           -------
           cube_areas - > float:
               calculate and return the cube surface area

           cube_circumferences - > float
               inherits the rectangle circumference method

           cube_circumradius(self):
                The radius of sphere circumscribed around a cube is called the circumradius.
                calculate and return the cube circumradius

           cube_center_point -> floats
               calculate and return the cube center point x,y, z

           cube_volume -> float
                calculate and return the cube volume

           move_cube -> x, y, z (floats)
               set the new coordinates to move the rectangle

           check_position -> Bool
               check if the point is within (return True) or outside (return False) the rectangle,
               the boundary is included

           __repr__ -> str
               return data (side1, x, y, z) for the cube

           __eq__ -> bool
               equality for side1, return True if equal, else False

           draw_cube
               plots the cube and the random point
       """

    def __init__(self, side1, x, y, z):
        super().__init__(side1, side1, x, y)
        self.z = z

        """ error handling """
        Rectangle.validate_length(side1)
        Rectangle.validate_real_numbers(x, y, z)

    def cube_areas(self):
        """
        :formula:  6 * a^2
        :return: cube surface area
        """
        cube_area = self.side1 * self.side1 * 6
        return cube_area

    def cube_circumferences(self):
        """
        :return: inherit rectangle circumference
        """
        return super().rectangle_circumferences()

    def cube_circumradius(self):
        """
        The radius of sphere circumscribed around a cube is called the circumradius.
        :formula: side * sqrt(3) / 2
        :return: circumradius
        """
        circumradius = self.side1 * math.sqrt(3) / 2
        return circumradius

    def cube_center_point(self):
        """
        calculate cube center point x, y, z
        :return: cube_center_x, cube_center_y, cube_center_z
        """
        cube_center_x = self.x + (self.side1/2)
        cube_center_y = self.y + (self.side1/2)
        cube_center_z = self.z + (self.side1/2)
        return cube_center_x, cube_center_y, cube_center_z

    def cube_volume(self):
        """
        calculate cube volume
        :return: volume
        """
        volume = math.pow(self.side1, 3)
        return volume

    def move_cube(self, move_x, move_y, move_z):
        """
        set the new coordinates to move the cube
        :param move_x: update self.x
        :param move_y: update self.y
        :param move_z: update self.z
        :return: self.x, self.y, self.z
        """
        self.x = move_x
        self.y = move_y
        self.z = move_z

    def check_pos_cube(self, point_x, point_y, point_z):
        """
        check if the point is within (True) or outside (False) the cube, the boundary is included

        :param point_x: random_point() set coordinate in x-direction
        :type point_x: int
        :param point_y: random_point() set coordinate in y-direction
        :type  point_y: int
        :param point_z: random_point() set coordinate in z-direction
        :type  point_z: int
        :return: bool
        """
        x1, x2 = self.x, self.x + self.side1
        y1, y2 = self.y, self.y + self.side1
        z1, z2 = self.z, self.z + self.side1

        if x1 <= point_x <= x2 and y1 <= point_y <= y2 and point_z <= z2:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        checks equality
        :param other: side1
        :return: bool
        """
        if isinstance(other, Rectangle):
            if other.side1 == self.side1:
                return True
            return False

    def __repr__(self):
        return f"Cube (side1 = {self.side1}, side1 = {self.side1} x = {self.x}, y = {self.y}, z = {self.z})"

    def draw_cube(self):
        """
        :link:  https://stackoverflow.com/questions/33540109/plot-surfaces-on-a-cube/33542678
        :changed: added dx, dy, dz for setting position
        :note: it uses the middle point to set the figure position
        :return: plot the cube
        """

        def get_cube():
            phi = np.arange(1, 10, 2) * np.pi / 4     # tar lite punkter för phi vinkeln
            phi2, theta = np.meshgrid(phi, phi)
            # Return coordinate matrices from coordinate vectors, in this case phi, phi and set as phi2, theta.

            x_cube = np.cos(phi2) * np.sin(theta)
            y_cube = np.sin(phi2) * np.sin(theta)
            z_cube = np.cos(theta) / np.sqrt(2)
            return x_cube, y_cube, z_cube

        dx, dy, dz = self.x, self.y, self.z
        fig = plt.figure()   # figure() = Create a new figure, or activate an existing figure.
        ax = fig.add_subplot(projection='3d')  # Create a figure and a set of subplots. Return fig , ax.
        # 3d projection to alert Matplotlib will get three dimensional data.

        # side lengths a, b, c
        a = self.side1
        b = self.side1
        c = self.side1
        x, y, z = get_cube()

        ax.plot_surface(x * a + dx, y * b + dy, z * c + dz, alpha=0.25)
        plt.plot(point_x, point_y, point_z, "ko")  # plot of coordinate for check_position()

        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_zlim(-15, 15)
        plt.show()


# objects
cube_1 = Cube(5, 0, 0, 0)
cube_2 = Cube(4, 1, 1, 1)

"""
# tests manual
print(cube_1)
print(cube_1.check_pos_cube(point_x, point_y, point_z))
print(cube_1.rectangle_areas())
print(cube_1.cube_circumferences())
print(cube_1.cube_circumradius())
print(cube_1.cube_center_point())
print(cube_1.cube_volume())
print(cube_1.draw_cube())
print(cube_1.move_cube(6, 6, 6))
print(cube_1.draw_cube())
print(cube_1.check_pos_cube(point_x, point_y, point_z))
"""

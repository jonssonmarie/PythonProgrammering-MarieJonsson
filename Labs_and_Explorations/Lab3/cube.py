"""
Class to create a geometric 3D cube
"""
import matplotlib.pyplot as plt
import numpy as np
import math

from rectangle import Rectangle

from random_coord import random_coordinates
point_x, point_y, point_z = random_coordinates()


class Cube(Rectangle):
    def __init__(self, side1, x, y, z):
        super().__init__(side1, side1, x, y)
        self.z = z

        # error handling
        Rectangle.validate_length(side1)  # class.static method behövs då den tillhör klassen self.static method när den är i methods
        Rectangle.validate_real_numbers(x, y, z)

    def cube_areas(self):
        # calculate cube surface area = 6 * a^2
        cube_area = self.side1 * self.side1 * 6
        return f"Cube area is: {cube_area} mm^2"

    def cube_circumferences(self):
        # calculate cube circumference = rectangle circumference
        return super().rectangle_circumferences()

    def cube_circumradius(self):
        # The radius of sphere circumscribed around a cube is called the circumradius.
        # calculate cube circumradius = side * sqrt(3) // 2
        circumradius = self.side1 * math.sqrt(3) // 2
        return f"Cube circumradius is: {circumradius} mm"

    def move_cube(self, move_x, move_y, move_z):
        # set the new coordinates to move the rectangle
        self.x = move_x
        self.y = move_y
        self.z = move_z
        return self.x, self.y, self.z

    def check_pos_cube(self, point_x, point_y, point_z):
        # check if the point within or outside the rectangle, the boundary is included
        x1, x2 = self.x, self.x + self.side1
        y1, y2 = self.y, self.y + self.side1
        z1, z2 = self.z, self.z + self.side1

        if x1 <= point_x <= x2 and y1 <= point_y <= y2 and point_z <= z2:
            return f"Point is within cube"
        else:
            return f"Point is outside cube"

    def __eq__(self, other):
        # checks equality by overloading ==
        if isinstance(other, Rectangle):
            if other.side1 == self.side1:
                return True
            return False

    def __repr__(self):
        return f"Cube = {self.side1} * {self.side1} * {self.side1}, Center point = ({self.x}, {self.y}, {self.z})"

    def draw_cube(self):
        # plot the cube      https://stackoverflow.com/questions/33540109/plot-surfaces-on-a-cube/33542678
        # added dx, dy, dz for setting position
        # it used the middle point to set the figure position

        def get_cube():
            phi = np.arange(1, 10, 2) * np.pi / 4
            phi2, theta = np.meshgrid(phi, phi)

            x = np.cos(phi2) * np.sin(theta)
            y = np.sin(phi2) * np.sin(theta)
            z = np.cos(theta) / np.sqrt(2)
            return x, y, z

        dx, dy, dz = self.x, self.y, self.z
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # side lengths a, b, c
        a = self.side1
        b = self.side1
        c = self.side1
        x, y, z = get_cube()

        ax.plot_surface(x * a + dx, y * b + dy, z * c + dz, alpha=0.25)
        plt.plot(point_x, point_y, point_z, "ko")

        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_zlim(-15, 15)
        plt.show()


# objects
cube_1 = Cube(5, 0, 0, 0)
cube_2 = Cube(4, 1, 1, 1)

# tests manual
print(cube_1)
print(cube_1.check_pos_cube(point_x, point_y, point_z))
print(cube_1.rectangle_areas())
print(cube_1.cube_circumferences())
print(cube_1.cube_circumradius())
print(cube_1.draw_cube())
print(cube_1.move_cube(6, 6, 6))
print(cube_1.draw_cube())
print(cube_1.check_pos_cube(point_x, point_y, point_z))

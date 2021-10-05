import matplotlib.pyplot as plt
import math
import numpy as np

from circle import Circle

from random_point import random_point
point_x, point_y, point_z = random_point()  # high jack in random_point() to set your own coordinates


class Sphere(Circle):
    """
    A class to create a geometric sphere

           Attributes
           ----------
           radius_circle : float
               radius of the circle
           x : float
               sphere start point in x direction
           y : float
               sphere start point in y direction
           z: float
                sphere start point in z direction

           Methods
           -------
           sphere_areas - > float:
               calculate and return the sphere surface area

           sphere_circumferences - > float
               inherits the circle circumference method

           sphere_center_point -> floats
               calculate and return the cube center point x,y, z

           sphere_volume -> float
                calculate and return the sphere volume

           move_sphere -> x, y, z (floats)
               set the new coordinates to move the sphere

           check_position -> Bool
               check if the point is within (return True) or outside (return False) the sphere,
               the boundary is included

           __repr__:
               return data (side1, x, y, z) for the sphere

           draw_sphere
               plots the sphere and the random point
           """
    def __init__(self, radius_circle, x, y, z):
        super().__init__(radius_circle, x, y)
        self.z = z

        # error handling
        Circle.validate_length(radius_circle)
        Circle.validate_real_numbers(x, y, z)

    def sphere_areas(self):
        """
        :formula:  4 * pi * r^2
        :return: sphere area """
        sphere_area = Circle.circle_areas(self) * 4
        return sphere_area

    def sphere_circumference(self):
        """
        :return: inherit circle_circumference
        """
        return super().circle_circumferences()

    def sphere_center_point(self):
        """
        :return: sphere center point x,y,z
        """
        return self.x, self.y, self.z

    def sphere_volume(self):
        """
        :formula: 4/3 * pi * r^3
        :return: volume
        """
        volume = 4/3 * math.pi * math.pow(self.radius_circle, 3)
        return volume

    def move_sphere(self, move_x, move_y, move_z):
        """set the new coordinates to move the sphere
        :param move_x: update self.x
        :param move_y: update self.y
        :param move_z: update self.z
        :return: self.x, self.y, self.z
        """
        self.x = move_x
        self.y = move_y
        self.z = move_z

    def check_pos_sphere(self, point_x, point_y, point_z):
        """
        check if the point is within (True) or outside (False) the sphere, the boundary is included

        :param point_x: random_point() set coordinate in x-direction
        :type point_x : float
        :param point_y: random_point() set coordinate in y-direction
        :type point_y: float
        :param point_z: random_point() set coordinate in z-direction
        :type point_z: float
        :formula: d^2 = (point_x - self.x)^2 + (point_y - self.y)^2 + (point_z - self.z)^2
        :return: bool
       """

        d3 = math.pow((point_x - self.x), 2) + math.pow((point_y - self.y), 2) + math.pow((point_z - self.z), 2)
        r2 = math.pow(self.radius_circle, 2)

        if d3 > r2:  # if d^2 > r^2 then outside the circle
            return True
        elif d3 <= r2:  # if d^2 <= r^2 then inside the circle
            return False

    def __eq__(self, other):
        """
        :param other: coordinate i z direction
        :return: bool
        """
        if isinstance(other, Sphere):
            if other.z == self.z and other.z == self.z:
                return True
            return False

    def __repr__(self):
        return f"Sphere (radius = {self.radius_circle}, x = {self.x}, y = {self.y}, z = {self.z})"

    def draw_sphere(self):
        """
        :return: plot the sphere
        """
        fig = plt.figure()  # figure() = Create a new figure, or activate an existing figure.

        ax = fig.add_subplot(1, 2, 1, projection='3d')  # Create a figure and a set of subplots. Return fig , ax.
        # 3d projection to alert Matplotlib will get three dimensional data.

        dx, dy, dz = self.x, self.y, self.z

        # Make data
        u = np.linspace(0, 2 * np.pi, 100)  # np.linspace - Return evenly spaced numbers over a specified interval.
        v = np.linspace(0, np.pi, 100)
        x = self.radius_circle * np.outer(np.cos(u), np.sin(v))  # np.outer - Compute the outer product of two vectors.
        y = self.radius_circle * np.outer(np.sin(u), np.sin(v))
        z = self.radius_circle * np.outer(np.ones(np.size(u)), np.cos(v))
        plt.plot(point_x, point_y, point_z, "ko")   # plot of coordinate for check_position()

        # subplot 1
        ax.set(xlim=(-15, 15), ylim=(-15, 15), zlim=(-15, 15))  # change range
        ax.plot_surface(x + dx, y + dy, z + dz)  # +dx etc adds the new position if it exist

        # subplot 2
        ax = fig.add_subplot(1, 2, 2, projection='3d')

        # plot wireframe with point
        ax.set(xlim=(-15, 15), ylim=(-15, 15), zlim=(-15, 15))   # change range
        ax.plot_wireframe(x + dx, y + dy, z + dz, rstride=10, cstride=10)  # +dx etc adds the new position if it exist
        # rstride, cstride - Downsampling stride in each direction, r - row, c - column, in this case it gives 10 lines
        # horisontally and vertically.
        plt.plot(point_x, point_y, point_z, "ko")

        plt.show()


# objects
sphere_1 = Sphere(4, 1, 1, 1)
sphere_2 = Sphere(5, 2, 1, 2)
"""
# tests manual
print(sphere_1)
print(sphere_1.sphere_areas())
print(sphere_1.sphere_circumference())
print(sphere_1.sphere_center_point())
print(sphere_1.sphere_volume())
print(sphere_1.check_pos_sphere(point_x, point_y, point_z))
print(sphere_1.draw_sphere())
print(sphere_1.move_sphere(5, 5, 5))
print(sphere_1.sphere_center_point())
print(sphere_1.draw_sphere())
print(sphere_1.check_pos_sphere(point_x, point_y, point_z))
"""

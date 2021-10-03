"""
Class to create a geometric 3D sphere
"""
import matplotlib.pyplot as plt
import math
import numpy as np

from circle import Circle

from random_point import random_point
point_x, point_y, point_z = random_point()  # high jack bye using # random_point() and add your own points eg. (1,2,3)


class Sphere(Circle):
    def __init__(self, radius_circle, x, y, z):
        super().__init__(radius_circle, x, y)
        self.z = z

        # error handling
        Circle.validate_length(radius_circle)  # class.static method behövs då den tillhör klassen self.static method när den är i methods
        Circle.validate_real_numbers(x, y, z)

    def sphere_areas(self):
        # calculate sphere area = 4 * pi * r^2
        sphere_area = 4 * math.pi * math.pow(self.radius_circle, 2)
        return f"Sphere area: {sphere_area:.2f} mm^2"

    def sphere_circumference(self):
        # calculate sphere circumference = circle circumference
        return super().circle_circumferences()

    def sphere_center_point(self):
        # sphere center point x,y,z
        return f"Center point (x,y, z): ({self.x}, {self.y}, {self.z})"

    def sphere_volume(self):
        # calculate sphere volume V ? 4/3 * pi * r^3
        volume = 4/3 * math.pi * math.pow(self.radius_circle,3)
        return f"Sphere volume = {volume:.2f} mm^3"

    def move_sphere(self, move_x, move_y, move_z):
        # set the new coordinates to move the rectangle
        self.x = move_x
        self.y = move_y
        self.z = move_z
        return self.x, self.y, self.z

    def check_pos_sphere(self, point_x, point_y, point_z):
        # check if the point is inside the sphere
        # d^2 = (coord_x - self.x)^2 + (coord_y - self.y)^2 + (coord_z - self.z)^2

        d3 = math.pow((point_x - self.x), 2) + math.pow((point_y - self.y), 2) + math.pow((point_z - self.z), 2)
        r2 = math.pow(self.radius_circle, 2)

        if d3 > r2:  # if d^2 > r^2 then outside the circle
            return f"Point is outside sphere"
        elif d3 <= r2:  # if d^2 <= r^2 then inside the circle
            return f"Point is within sphere"

    def __eq__(self, other):
        # checks equality by overloading ==
        if isinstance(other, Sphere):
            if other.z == self.z and other.z == self.z:
                return True
            return False

    def __repr__(self):
        return f"Sphere data: radius = {self.radius_circle}, Center point = ({self.x}, {self.y}, {self.z})"

    def draw_sphere(self):
        # plot the sphere
        fig = plt.figure()

        ax = fig.add_subplot(1, 2, 1, projection='3d')

        dx, dy, dz = self.x, self.y, self.z

        # Make data
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = self.radius_circle * np.outer(np.cos(u), np.sin(v))
        y = self.radius_circle * np.outer(np.sin(u), np.sin(v))
        z = self.radius_circle * np.outer(np.ones(np.size(u)), np.cos(v))
        plt.plot(point_x, point_y, point_z, "ko")

        # subplot 1
        ax.set(xlim=(-15, 15), ylim=(-15, 15), zlim=(-15, 15))  # change range
        ax.plot_surface(x + dx, y + dy, z + dz)

        # subplot 2
        ax = fig.add_subplot(1, 2, 2, projection='3d')

        # plot wireframe with point
        ax.set(xlim=(-15, 15), ylim=(-15, 15), zlim=(-15, 15))   # change range
        ax.plot_wireframe(x + dx, y + dy, z + dz, rstride=10, cstride=10)
        plt.plot(point_x, point_y, point_z, "ko")

        plt.show()


# objects
sphere_1 = Sphere(4, 1, 1, 1)
sphere_2 = Sphere(5, 2, 1, 2)

# tests manual
print(sphere_1)
print(sphere_1.sphere_areas())
print(sphere_1.sphere_circumference())
print(sphere_1.sphere_center_point())
print(sphere_1.sphere_volume())
print(sphere_1.check_pos_sphere(point_x, point_y, point_z))
print(sphere_1.draw_sphere())
print("New coordinates: ",sphere_1.move_sphere(5, 5, 5))
print(sphere_1.sphere_center_point())
print(sphere_1.draw_sphere())
print(sphere_1.check_pos_sphere(point_x, point_y, point_z))

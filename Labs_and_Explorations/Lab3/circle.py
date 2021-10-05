import matplotlib.pyplot as plt
import math

from random_point import random_point
point_x, point_y, point_z = random_point()  # high jack in random_point() to set your own coordinates


class Circle:
    """
     A class to create a geometric circle

            Attributes
            ----------
            radius_circle : float
                radius of the circle
            x : float
                rectangle start point in x direction
            y : float
                rectangle start point in y direction

            Methods
            -------
            circle_areas - > float:
                calculates and return the circle area

            circle_circumferences - > float
                calculates the and return circle circumference

            circle_center_point -> floats
                calculate and return the circle center point x,y

            move_circle -> x, y (float)
                set the new coordinates to move the circle

            check_position -> Bool
                check if the point is within (return True) or outside (return False) the circle,
                the boundary is included

            @staticmethod
            validate_length -> tuple
                Validate if length is positive, return value else raise ValueError

            @staticmethod
            validate_real_numbers  -> tuple
                Validate if value is int or float, return value else raise TypeError

            __repr__ -> str
                return data (radius_circle, x, y) for the circle

            __eq__ ->
                equality for radius_circle, return True if equal, else False

            draw_circle
                plots the circle and the random point
        """

    def __init__(self, radius_circle, x, y):
        """
        :param radius_circle: circle radius
        :type radius_circle: float
        :param x: circle start point in x direction
        :param y: sphere start point in y direction
        """
        self.radius_circle = radius_circle
        self.x = x
        self.y = y

        # error handling
        Circle.validate_length(radius_circle)
        Circle.validate_real_numbers(radius_circle, x, y)

    def circle_areas(self):
        """
        :formula: pi * r^2
        :return: circle area
        """
        circle_area = math.pi * math.pow(self.radius_circle, 2)
        return circle_area

    def circle_circumferences(self):
        """
        :formula: pi * 2 * r
        :return: circle circumference
        """
        circle_circumference = 2 * math.pi * self.radius_circle
        return circle_circumference

    def circle_center_point(self):
        """
        circle center point x, y
        :return: self.x, self.y,
        """
        return self.x, self.y

    def move_circle(self, move_x, move_y):
        """ set the new coordinates to move the circle
        :param move_x: update self.x
        :param move_y: update self.y
        :return: self.x, self.y
        """
        self.x = move_x
        self.y = move_y

    def check_position(self, point_x, point_y):
        """
        check if the point is inside the circle True, else False. Boundary is included within.
        formula: d^2 = (point_x - self.x)^2 + (point_y - self.y)^2

        :param point_x: random_point() set coordinate in x-direction
        :type point_x : float
        :param point_y: random_point() set coordinate in y-direction
        :type point_y: float
        :return: bool
        """
        d2 = math.pow((point_x - self.x), 2) + math.pow((point_y - self.y), 2)
        r2 = math.pow(self.radius_circle, 2)
        if d2 > r2:                          # if d^2 > r^2 then outside the circle
            return False
        elif d2 <= r2:                       # if d^2 <= r^2 then inside the circle
            return True

    @staticmethod
    def validate_length(*value) -> tuple:
        """  Validate if length is positive
        :param value: radius_circle
        :return: value
        """
        for val in value:
            if val <= 0:
                raise ValueError(f"Length must be > 0 not {val}")
            Circle.validate_real_numbers(val)
        return value

    @staticmethod
    def validate_real_numbers(*value) -> tuple:
        """
        Validate if value is int or float
        :param value: radius_circle, x, y
        :return: value
        """
        for val in value:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Positions must be in or float not {type(val)}")
        return value

    def __eq__(self, other):
        """
        checks equality by overloading ==
        :param other: radius_circle
        :return: bool
        """
        if isinstance(other, Circle):
            if other.radius_circle == self.radius_circle:
                return True
            return False

    def __repr__(self):
        return f"Circle (radius = {self.radius_circle}, x = {self.x}, y = {self.y})"

    def draw_circle(self):
        """
        :return: plot the circle
        """
        drawing_circle = plt.Circle((self.x, self.y), self.radius_circle, color="blue", fill=False, linewidth=3)
        # Patches class Circle - Create a true circle at center xy = (x, y) with given radius, include Figure()

        ax = plt.gca()  # Get the current Axes instance on the current figure matching the given keyword args.

        ax.set(xlim=(-15, 15), ylim=(-15, 15))  # change range
        ax.add_patch(drawing_circle)            # adds a Patch to the axes’ patches, return patch
        ax.plot(point_x, point_y, "ko")         # plot of coordinate for check_position()
        ax.set_aspect("equal", "box")           # make scale equal
        plt.show()                              # Display all open figures.

"""
# objects
circle_1 = Circle(5, 1, 1)
circle_2 = Circle(6, 2, 3)

# tests manual
print(circle_1)
print(circle_1.circle_areas())
print(circle_1.circle_circumferences())
print(circle_1.circle_center_point())
print(circle_1.check_position(point_x, point_y))
print(f"circle_1 == circle_2 : {circle_1 == circle_2}")
print(circle_1.draw_circle())
print(circle_1.move_circle(5,5))
print(circle_1.circle_center_point())
print(circle_1.draw_circle())
print(circle_1.check_position(point_x, point_y))
"""
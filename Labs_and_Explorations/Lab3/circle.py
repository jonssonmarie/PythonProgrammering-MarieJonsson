"""
Class to create a geometric Circle
"""
import matplotlib.pyplot as plt
import math

from random_point import random_point
point_x, point_y, point_z = random_point()  # high jack bye using # random_point() and add your own points eg. 1,2,3


class Circle:
    def __init__(self, radius_circle, x, y):
        self.radius_circle = radius_circle
        self.x = x
        self.y = y

        # error handling
        Circle.validate_length(radius_circle)  # class.static method behövs då den tillhör klassen self.static method när den är i methods
        Circle.validate_real_numbers(radius_circle, x, y)

    def circle_areas(self):
        # calculate circle area A = pi * r^2
        circle_area = math.pi * math.pow(self.radius_circle, 2)
        return f"Circle area: {circle_area:.2f} mm^2"

    def circle_circumferences(self):
        # calculate circle circumference = pi * 2 * r
        circle_circumference = 2 * math.pi * self.radius_circle
        return f"Circumferences: {circle_circumference:.2f} mm"

    def circle_center_point(self):
        # circle center point x,y,z
        return f"Center point (x,y): ({self.x}, {self.y})"

    def move_geometry_circle(self, move_x, move_y):
        # set the new coordinates to move the rectangle
        self.x = move_x
        self.y = move_y
        return self.x, self.y

    def check_position(self, point_x, point_y):
        """ check if the point is inside the circle
            d^2 = (coord_x - self.x)^2 + (coord_y - self.y)^2
        """
        d2 = math.pow((point_x - self.x), 2) + math.pow((point_y - self.y), 2)
        r2 = math.pow(self.radius_circle, 2)
        if d2 > r2:                                     # if d^2 > r^2 then outside the circle
            return f"Point is outside circle"
        elif d2 <= r2:                                   # if d^2 <= r^2 then inside the circle
            return f"Point is within circle"

    @staticmethod
    def validate_length(*value) -> tuple:
        """  Validate if length is positive """
        for val in value:
            if val <= 0:
                raise ValueError(f"Length must be > 0 not {val}")
            Circle.validate_real_numbers(val)
        return value

    @staticmethod
    def validate_real_numbers(*value) -> tuple:
        """ Validate if value is int or float """
        for val in value:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Positions must be in or float not {type(val)}")
        return value

    def __eq__(self, other):
        # checks equality by overloading ==
        if isinstance(other, Circle):
            if other.radius_circle == self.radius_circle:
                return True
            return False

    def __repr__(self):
        return f"Circle data: radius = {self.radius_circle}, Center point = ({self.x}, {self.y})"

    def draw_circle(self):
        # plot the circle
        drawing_circle = plt.Circle((self.x, self.y), self.radius_circle, color="blue", fill=False, linewidth=3)

        fig, ax = plt.subplots(figsize=(12, 6))

        fig = plt.gcf()  # Get the current figure. If no current figure exists, a new one is created using figure().
        ax = plt.gca()   # Get the current Axes instance on the current figure matching the given keyword args, or create one.

        # change range
        ax.set(xlim=(-15,15), ylim=(-15,15))

        ax.add_patch(drawing_circle)
        ax.plot(point_x, point_y, "ko")         # plot of coordinate for check_position()
        ax.set_aspect("equal", "box")           # make scale equal
        plt.show()


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
print("New coordinates: ", circle_1.move_geometry_circle(5,5))
print(circle_1.circle_center_point())
print(circle_1.draw_circle())
print(circle_1.check_position(point_x, point_y))

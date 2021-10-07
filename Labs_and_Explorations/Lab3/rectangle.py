import matplotlib.pyplot as plt

from random_point import random_point
point_x, point_y, point_z = random_point()  # high jack in random_point() to set your own coordinates


class Rectangle:
    """
     A class to create a geometric rectangle

            Attributes
            ----------
            side1 : float
                base of the rectangle
            side2 : float
                height of the rectangle
            x : float
                rectangle start point in x direction
            y : float
                rectangle start point in y direction

            Methods
            -------
            area - > float:
                calculates the rectangle area

            circumferences - > float
                calculates the rectangle circumference

            center_point -> floats
                calculate the rectangle center point x,y

            move_geometry -> x, y (float)
                set the new coordinates to move the rectangle

            check_position -> Bool
                check if the point is within (True) or outside (False) the rectangle, the boundary is included

            @staticmethod
            validate_length -> tuple
                Validate if length is positive, return value else raise ValueError

            @staticmethod
            validate_real_numbers  -> tuple
                Validate if value is int or float, return value else raise TypeError

            __repr__ - > str
                return data (side1, side2, x, y) for the rectangle

            __eq__ - > bool
                 equality for side1, side2, return True if equal, else False

            draw_2d_geometry -> Figure
                plots the rectangle and the random point
    """

    def __init__(self, side1, side2, x, y):
        self.side1 = side1
        self.side2 = side2
        self.x = x
        self.y = y

        ''' error handling '''
        Rectangle.validate_length(side1, side2)
        Rectangle.validate_real_numbers(x, y)

    def area(self):
        """
        calculate rectangle area
        :formula: side * side
        :return: rectangle_area
        """
        rectangle_area = self.side1 * self.side2
        return rectangle_area

    def circumferences(self):
        """
        calculate rectangle circumference
        :return: rectangle_circumference
        """
        rectangle_circumference = self.side1 * 2 + self.side2 * 2
        return rectangle_circumference

    def center_point(self):
        """
        rectangle center point x, y
        :return: rectangle_center_x, rectangle_center_y
        """
        rectangle_center_x = self.x + (self.side1/2)
        rectangle_center_y = self.y + (self.side2/2)
        return rectangle_center_x, rectangle_center_y

    def move_geometry(self, move_x, move_y):
        """
        set the new coordinates to move the rectangle
        :param move_x: update self.x
        :param move_y: update self.y
        :return: self.x, self.y
        """
        self.x = move_x
        self.y = move_y

    def check_position(self, point_x, point_y):
        """
        check if the point within (True) or outside (False) the rectangle, the boundary is included

        :param point_x: random_point() set coordinate in x-direction
        :type point_x : float
        :param point_y: random_point() set coordinate in y-direction
        :type point_x : float
        :return: bool
        """

        x1, x2 = self.x, self.x + self.side1
        y1, y2 = self.y, self.y + self.side2

        if x1 <= point_x <= x2 and y1 <= point_y <= y2:
            return True
        else:
            return False

    @staticmethod
    def validate_length(*value) -> tuple:
        """ Validate if length is positive
        :param value: side1, side2
        :return: value
        """
        for val in value:
            if val <= 0:
                raise ValueError(f"Length must be > 0 not {val}")
            Rectangle.validate_real_numbers(val)
        return value

    @staticmethod
    def validate_real_numbers(*value) -> tuple:
        """
        Validate if value is int or float
        :param value: side1, side2, x, y
        :return: value
        """
        for val in value:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Numbers must be in or float not {type(val)}")
        return value

    def __eq__(self, other):
        """
        checks equality True if equal, else False
        :param other: side1, side2
        :return: bool
        """
        if isinstance(other, Rectangle):
            if other.side1 == self.side1 and other.side2 == self.side2:
                return True
            elif other.side1 == self.side2 or other.side2 == self.side1:
                return True
            return False

    def __repr__(self):
        return f"Rectangle (side1 = {self.side1}, side2 = {self.side2} x = {self.x}, y = {self.y})"

    def draw_2d_geometry(self):
        """
        :return: plot the rectangle
        """
        drawing_rectangle = plt.Rectangle((self.x, self.y), self.side1, self.side2, color="red", fill=False,
                                          linewidth=2)
        # Patches class Rectangle - A rectangle defined via an anchor point xy and its width and height.
        # Include figure()

        ax = plt.gca()  # Get the current Axes instance on the current figure matching the given keyword args,
                        # or create one.

        ax.set(xlim=(-15, 15), ylim=(-15, 15))   # set x, y axis limits

        ax.add_patch(drawing_rectangle)    # adds a Patch to the axes’ patches, return patch
        ax.plot(point_x, point_y, "ko")    # plot the point for check_position()

        ax.set_aspect("equal", "box")      # make scale equal
        plt.show()                         # Display all open figures.


# objects
rectangle_1 = Rectangle(5, 10, 1, 1)
rectangle_2 = Rectangle(3, 3, 2, 3)
rectangle_3 = Rectangle(4, 1, -2, -3)
"""
# tests manual
print(rectangle_1)
print(rectangle_1.area())
print(rectangle_1.circumferences())
print(rectangle_1.center_point())
print(rectangle_1.check_position(point_x, point_y))
print(f"rectangle_1 == rectangle_2 : {rectangle_1 == rectangle_2}")
print(rectangle_1.draw_2d_geometry())
print(rectangle_1.move_geometry(-5, -5))
print(rectangle_1)
print(rectangle_1.check_position(point_x, point_y))
print(rectangle_1.center_point())
print(rectangle_1.draw_2d_geometry())
print("--------------")
""""

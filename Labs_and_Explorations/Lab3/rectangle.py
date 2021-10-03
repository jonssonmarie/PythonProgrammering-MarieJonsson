"""
Class to create a geometric rectangle
"""
import matplotlib.pyplot as plt

from random_point import random_point
point_x, point_y, point_z = random_point()  # high jack bye using # random_point() and add your own points eg. (1,2,3)


class Rectangle:
    def __init__(self, side1, side2, x, y):
        self.side1 = side1
        self.side2 = side2
        self.x = x
        self.y = y

        # error handling
        Rectangle.validate_length(side1, side2)  # class.static method behövs då den tillhör klassen
        Rectangle.validate_real_numbers(x, y)

    def rectangle_areas(self):
        # calculate rectangle area
        rectangle_area = self.side1 * self.side2
        return f"Rectangle area = {rectangle_area} mm^2"

    def rectangle_circumferences(self):
        # calculate rectangle circumference
        rectangle_circumference = self.side1 * 2 + self.side2 * 2
        return f"Circumferences: {rectangle_circumference:.2f} mm"

    def rectangle_center_point(self):
        # calculate rectangle center point x,y
        rectangle_center_x = self.x + (self.side1/2)
        rectangle_center_y = self.y + (self.side2/2)
        return f"Center point (x,y): ({rectangle_center_x}, {rectangle_center_y})"

    def move_rectangle(self, move_x, move_y):
        # set the new coordinates to move the rectangle
        self.x = move_x
        self.y = move_y
        return self.x, self.y

    def check_position(self, point_x, point_y):
        # check if the point within or outside the rectangle, the boundary is included
        x1, x2 = self.x, self.x + self.side1
        y1, y2 = self.y, self.y + self.side2

        if x1 <= point_x <= x2 and y1 <= point_y <= y2:
            return f"Point is within rectangle"
        else:
            return f"Point is outside rectangle"

    @staticmethod
    def validate_length(*value) -> tuple:
        #  Validate if length is positive
        for val in value:
            if val <= 0:
                raise ValueError(f"Length must be > 0 not {val}")
            Rectangle.validate_real_numbers(val)
        return value

    @staticmethod
    def validate_real_numbers(*value) -> tuple:
        # Validate if value is int or float
        for val in value:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Numbers must be in or float not {type(val)}")
        return value

    def __eq__(self, other):
        # checks equality by overloading ==
        if isinstance(other, Rectangle):
            if other.side1 == self.side1 and other.side2 == self.side2:
                return True
            elif other.side1 == self.side2 or other.side2 == self.side1:
                return True
            return False

    def __repr__(self):
        return f"Rectangle data: sideA * sideB: {self.side1} * {self.side2}, Start point: ({self.x}, {self.y})"

    def draw_rectangle(self):
        # plot the rectangle
        drawing_rectangle = plt.Rectangle((self.x, self.y), self.side1, self.side2, color="red", fill=False, linewidth=2)

        fig, ax = plt.subplots(figsize=(12,6))
        ax = plt.gca()
        # Get the current Axes instance on the current figure matching the given keyword args, or create one.

        # set x, y axis limits
        ax.set(xlim=(-15, 15), ylim=(-15, 15))

        ax.add_patch(drawing_rectangle)
        ax.plot(point_x, point_y, "ko")    # plot the point for check_position()

        ax.set_aspect("equal", "box")      # make scale equal
        plt.show()


# objects
rectangle_1 = Rectangle(5,10, 1, 1)
rectangle_2 = Rectangle(3, 3, 2, 3)
rectangle_3 = Rectangle(4, 1, -2, -3)

# tests manual
print(rectangle_1)
print(rectangle_1.rectangle_areas())
print(rectangle_1.rectangle_circumferences())
print(rectangle_1.rectangle_center_point())
print(rectangle_1.check_position(point_x, point_y))
print(f"rectangle_1 == rectangle_2 : {rectangle_1 == rectangle_2}")
print(rectangle_1.draw_rectangle())
print("New coordinates",rectangle_1.move_rectangle(-5, -5))
print(rectangle_1)
print(rectangle_1.check_position(point_x, point_y))
print(rectangle_1.rectangle_center_point())
print(rectangle_1.draw_rectangle())
print("--------------")

# tests manual
"""
print(rectangle_2)
print(rectangle_2.rectangle_areas())
print(rectangle_2.rectangle_circumferences())
print(rectangle_2.rectangle_center_point())
print(rectangle_2.check_position(point_x, point_y))
print(f"rectangle_1 == rectangle_3 : {rectangle_1 == rectangle_3}")
print(rectangle_2.draw_rectangle())                                  # varför hålla koll på mittpunkt? Kokchun
print(rectangle_2.move_rectangle(-5, -5))
print(rectangle_2)
print(rectangle_2.check_position(point_x, point_y))
print(rectangle_2.rectangle_center_point())
print(rectangle_2.draw_rectangle())
"""

import matplotlib.pyplot as plt
import math
import numpy as np

from random_coord import random_coordinates
coord_x, coord_y, coord_z = random_coordinates()


class Circle:
    def __init__(self, radius_circle, x, y):
        self.radius_circle = radius_circle
        self.x = x
        self.y = y

        # error handling
        Circle.validate_length(radius_circle)  # class.static method behövs då den tillhör klassen self.static method när den är i methods
        Circle.validate_real_numbers(radius_circle, x, y)

    def circle_areas(self):
        circle_area = math.pi * math.pow(self.radius_circle, 2)
        return f"Circle area: {circle_area:.2f} mm^2"

    def circle_circumferences(self):
        circle_circumference = 2 * math.pi * self.radius_circle
        return f"Circumferences: {circle_circumference:.2f} mm"

    def check_position(self, coord_x, coord_y):
        """ check if the coord_x, coord_y is inside the circle
            d^2 = (coord_x - self.x)^2 + (coord_y - self.y)^2
        """
        d2 = math.pow((coord_x - self.x), 2) + math.pow((coord_y - self.y), 2)
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

    def move_geometry_circle(self, move_x, move_y):
        self.x = move_x
        self.y = move_y
        return self.x, self.y

    def __eq__(self, other):
        # checks equality by overloading ==
        if isinstance(other, Circle):
            if other.radius_circle == self.radius_circle:
                return True
            return False

    def __repr__(self):
        return f"Circle data: radius = {self.radius_circle}, Center point = ({self.x}, {self.y})"

    def draw_circle(self):
        drawing_circle = plt.Circle((self.x, self.y), self.radius_circle, color="blue", fill=False, linewidth=3)
                          # .Circle((x,y för mittpunkt), radius, **kwargs

        fig, ax = plt.subplots(figsize=(12, 6))  # varför ska fig vara med när bara en bild i taget. Fattar inte hur man uppdaterar en sparad bild

        #fig = plt.gcf()  # Get the current figure. If no current figure exists, a new one is created using figure().
        ax = plt.gca()   # Get the current Axes instance on the current figure matching the given keyword args, or create one.

        # change range
        ax.set(xlim=(-5,10), ylim=(-5,10))

        ax.add_patch(drawing_circle)
        ax.plot(coord_x, coord_y, "ko")         # plot of coordinate for check_position()
        ax.set_aspect("equal", "box")           # make scale equal
        #plt.savefig("files/circle.png", transparent=True, facecolor="white")
        plt.show()


class Rectangle:
    def __init__(self, side1, side2, x, y):
        self.side1 = side1
        self.side2 = side2
        self.x = x
        self.y = y

        # error handling
        Rectangle.validate_length(side1, side2)  # class.static method behövs då den tillhör klassen self.static method när den är i methods
        Rectangle.validate_real_numbers(x, y)

    def rectangle_areas(self):
        rectangle_area = self.side1 * self.side2
        return f"Rectangle area = {rectangle_area} mm^2"

    def rectangle_circumferences(self):
        rectangle_circumference = self.side1 * 2 + self.side2 * 2
        return f"Circumferences: {rectangle_circumference:.2f} mm"

    def move_geometry_rectangle(self, move_x, move_y):
        self.x = move_x
        self.y = move_y
        return self.x, self.y

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            if other.side1 == self.side1 and other.side2 == self.side2:
                return True
            return False

    def __repr__(self):
        return f"Rectangle data: sideA * sideB: {self.side1} * {self.side2}, Start point: ({self.x}, {self.y})"

    @staticmethod
    def validate_length(*value) -> tuple:
        #  Validate if length is positive
        for val in value:
            if val <= 0:
                raise ValueError(f"Length must be > 0 not {val}")
            Circle.validate_real_numbers(val)
        return value

    @staticmethod
    def validate_real_numbers(*value) -> tuple:
        # Validate if value is int or float
        for val in value:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Numbers must be in or float not {type(val)}")
        return value

    def check_position(self, coord_x, coord_y):
        x1, x2 = self.x, self.x + self.side1
        y1, y2 = self.y, self.y + self.side2

        if x1 <= coord_x <= x2 and y1 <= coord_y <= y2:
            return f"Point is within rectangle"
        else:
            return f"Point is outside rectangle"

    def draw_rectangle(self):
        drawing_rectangle = plt.Rectangle((self.x,self.y), self.side1, self.side2, color="red", fill=False, linewidth=2)
         # Rectangle((x,y left lower corner), width, height, angle= 0.0, **kwargs
        fig2, ax2 = plt.subplots(1, figsize=(12,6))

        fig2 = plt.gcf()
        ax2 = plt.gca()                     #.set_aspect('equal', adjustable='box')

        # set x, y axis limits
        ax2.set(xlim=(-5,15), ylim=(-5,15))

        ax2.add_patch(drawing_rectangle)
        ax2.plot(coord_x, coord_y, "ko")    # plot of coordinate for check_position()

        ax2.set_aspect("equal", "box")      # make scale equal
        plt.show()


class Sphere(Circle):
    def __init__(self, radius_circle, x, y, z):
        super().__init__(radius_circle, x, y)
        self.z = z

        # error handling
        Circle.validate_length(radius_circle)  # class.static method behövs då den tillhör klassen self.static method när den är i methods
        Circle.validate_real_numbers(x, y, z)

    def sphere_areas(self):
        sphere_area = 4 * math.pi * self.radius_circle
        return f"Sphere area: {sphere_area:.2f} mm^2"

    def sphere_circumference(self):
        return super().circle_circumferences()
    
    def move_geometry_sphere(self, move_x, move_y, move_z):
        self.x = move_x
        self.y = move_y
        self.z = move_z
        return self.x, self.y, self.z

    def check_pos_sphere(self, coord_x, coord_y, coord_z):
        # check if the coord_x, coord_y, coord_z is inside the sphere
        # d^2 = (coord_x - self.x)^2 + (coord_y - self.y)^2 + (coord_z - self.z)^2
        
        d3 = math.pow((coord_x - self.x), 2) + math.pow((coord_y - self.y), 2) + math.pow((coord_z - self.z), 2)
        r2 = math.pow(self.radius_circle, 2)
        print("d3", d3)
        print("r2", r2)
        if d3 > r2:  # if d^2 > r^2 then outside the circle
            return f"Point is outside sphere"
        elif d3 <= r2:  # if d^2 <= r^2 then inside the circle
            return f"Point is within sphere"

    def __eq__(self, other):
        if isinstance(other, Sphere):
            if other.z == self.z and other.z == self.z:
                return True
            return False

    def __repr__(self):
        return f"Sphere data: radius = {self.radius_circle}, Center point = ({self.x}, {self.y}, {self.z})"

    def draw_sphere(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,2,1, projection='3d')

        dx, dy, dz = self.x, self.y, self.z

        # Make data
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = self.radius_circle * np.outer(np.cos(u), np.sin(v))
        y = self.radius_circle * np.outer(np.sin(u), np.sin(v))
        z = self.radius_circle * np.outer(np.ones(np.size(u)), np.cos(v))
        plt.plot(coord_x, coord_y, coord_z, "ko")

        # subplot 1
        ax.plot_surface(x + dx, y + dy, z + dz)

        # subplot 2
        ax = fig.add_subplot(1, 2, 2, projection='3d')

        # plot wireframe with point
        ax.plot_wireframe(x + dx, y + dy, z + dz, rstride=10, cstride=10)
        plt.plot(coord_x, coord_y, coord_z, "ko")
        plt.show()


class Cube(Rectangle):
    def __init__(self, side1, side2, x, y, z):                   # Fråga varför side2 måste vara med för att funka
        super().__init__(side1, side2, x, y)
        self.z = z

        # error handling
        Rectangle.validate_length(side1, side2)  # class.static method behövs då den tillhör klassen self.static method när den är i methods
        Rectangle.validate_real_numbers(x, y, z)

    def cube_areas(self):
        cube_area = self.side1 * self.side1 * 4
        return f"Cube area is: {cube_area} mm^2"

    def cube_circumferences(self):
        return super().rectangle_circumferences()

    def check_pos_cube(self, coord_x, coord_y, coord_z):
        x1, x2 = self.x, self.x + self.side1
        y1, y2 = self.y, self.y + self.side1
        z1, z2 = self.z, self.z + self.side1

        if x1 <= coord_x <= x2 and y1 <= coord_y <= y2 and coord_z <= z2:
            return f"Point is within cube"
        else:
            return f"Point is outside cube"

    def move_geometry_cube(self, move_x, move_y, move_z):
        self.x = move_x
        self.y = move_y
        self.z = move_z
        return self.x, self.y, self.z

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            if other.side1 == self.side1:
                return True
            return False

    def __repr__(self):
        return f"Cube = {self.side1} * {self.side1} * {self.side1}, Center point = ({self.x}, {self.y}, {self.z})"

    def draw_cube(self):   
        # Utgår den från kubens 0,0,0 i ena hörnet sedan växer åt positivt håll
        # vid move flyttar den efter mittpunkten
        # https://stackoverflow.com/questions/33540109/plot-surfaces-on-a-cube/33542678
        # added dx, dy, dz for setting position

        def get_cube():
            phi = np.arange(1, 10, 2) * np.pi / 4
            Phi, Theta = np.meshgrid(phi, phi)

            x = np.cos(Phi) * np.sin(Theta)
            y = np.sin(Phi) * np.sin(Theta)
            z = np.cos(Theta) / np.sqrt(2)
            return x, y, z

        dx, dy, dz = self.x, self.y, self.z
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # edge lengths a, b, c
        a = self.side1
        b = self.side1
        c = self.side1
        x, y, z = get_cube()

        ax.plot_surface(x * a + dx, y * b + dy, z * c + dz, alpha=0.25)
        plt.plot(coord_x, coord_y, coord_z, "ko")

        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_zlim(-10, 10)
        plt.show()


# objects
circle_1 = Circle(5, 1, 7)
circle_2 = Circle(6, 2, 3)
rectangle_1 = Rectangle(8, 7, 1, 1)
rectangle_2 = Rectangle(3, 3, 2, 3)
sphere_1 = Sphere(4, 1, 1, 1)
sphere_2 = Sphere(5, 2, 1, 2)
cube_1 = Cube(5,5, 0, 0, 0)  # x, y utgår i mittpunkten på kuben
cube_2 = Cube(4,4, 1, 1, 1)

"""

# tests manual
print(circle_1)
print(circle_1.circle_areas())
print(circle_1.circle_circumferences())
print(circle_1.check_position(coord_x, coord_y))
print(f"circle_1 == circle_2 : {circle_1 == circle_2}")
#print(circle_1.draw_circle())   # går på mittpunkten
print(circle_1.move_geometry(5,5))
#print(circle_1.draw_circle())

print("------------------------------------")

print(rectangle_1)
print(rectangle_1.rectangle_areas())
print(rectangle_1.rectangle_circumferences())
print(rectangle_1.check_position(coord_x, coord_y))
print(f"rectangle_1 == rectangle_2 : {rectangle_1 == rectangle_2}")
print(rectangle_1.draw_rectangle())  # utgår nedre vä hörnet som referens    # varför hålla koll på mittpunkt? Kokchun
print(rectangle_1.move_geometry(5,5))
print(rectangle_1.draw_rectangle())

print("-------------------------------------")
print(sphere_1)
print(sphere_1.sphere_areas())
print(sphere_1.sphere_circumference())
print(sphere_1.check_pos_sphere(coord_x, coord_y, coord_z))
print(sphere_1.draw_sphere())                       # utgår från mittpunkten
print(sphere_1.move_geometry_sphere(5, 5, 5))
print(sphere_1.draw_sphere())
print(sphere_1.check_pos_sphere(coord_x, coord_y, coord_z))

print("-------------------------------------")
print(cube_1)
print(cube_1.check_pos_cube(coord_x, coord_y, coord_z))
print(cube_1.rectangle_areas())
print(cube_1.cube_circumferences())
print(cube_1.draw_cube())
print(cube_1.move_geometry_cube(6,6,6))
print(cube_1.draw_cube())
print(cube_1.check_pos_cube(coord_x, coord_y, coord_z))
"""


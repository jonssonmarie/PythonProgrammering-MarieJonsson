"""
Unit testing for Lab 3
"""
import unittest
from lab_3 import Circle
from lab_3 import Rectangle
from lab_3 import Sphere
from lab_3 import Cube


class Lab3Circle(unittest.TestCase):
    def setUp(self) -> None:
        self.radius_circle, self.x, self.y = 5, 1, 3

    def create_circle(self) -> "Circle":
        return Circle(self.radius_circle, self.x, self.y)

    def test_create_circle(self):
        c1 = self.create_circle()
        c2 = Circle(5, 1, 3)
        self.assertEqual(c1, c2)  # förväntas att argumenten är lika

    def test_create_empty_circle(self):
        with self.assertRaises(TypeError):  # vi förväntar oss att vi testar en Exception (via self.assertRaises) om inte så failar vi
            c = Circle()

    def test_create_invalid_circle(self):
        with self.assertRaises(TypeError):
            c = Circle(5, 1, "a") #"a")

    def test_two_circle_not_equal(self) -> None:
        c1 = self.create_circle()
        c2 = self.create_circle()
        self.assertAlmostEqual(c1, c2)

    def test_circle_minus_radius(self) -> None:
        with self.assertRaises(ValueError):
            c = Circle(-1, 2, 7)

    def test_area(self):
        c1 = self.create_circle()
        c2 = Circle(5, 1, 3)
        self.assertAlmostEqual(c1, c2)


"""
class Lab3Rectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.side1, self.side2, self.x , self.y = 4, 3, 4, 6

    def create_rectangle(self) -> "Rectangle":
        return Rectangle(self.side1, self.side2, self.x, self.y)

    def test_create_rectangle(self):
        c1 = self.create_rectangle()
        c2 = Rectangle(3, 4, 1, 2)
        self.assertEqual(c1, c2)  # förväntas att argumenten är lika

    def test_create_empty_rectangle(self):
        with self.assertRaises(ValueError):  # vi förväntar oss att vi testar en Exception (via self.assertRaises) om inte så failar vi
            v = Rectangle()

    def test_create_invalid_rectangle(self):
        with self.assertRaises(TypeError):
            v = Rectangle(5, 4, 1, 2) #"a")

    def test_two_rectangle_not_equal(self) -> None:
        v1 = self.create_rectangle()
        v2 = Rectangle(10, 2, 3,-7)
        self.assertNotEqual(v1, v2)

    def test_rectangle_minus_lenghts(self) -> None:
        with self.assertRaises(ValueError):
            v = Rectangle(-1, 3, 2, 7)


class Lab3Sphere(unittest.TestCase):
    def setUp(self) -> None:
        self.radius_circle, self.x, self.y, self.z = 3, 2, 4, 2

    def create_sphere(self) -> "Sphere":
        return Sphere(self.radius_circle, self.x, self.y, self.z)

    def test_create_sphere(self):
        c1 = self.create_sphere()
        c2 = Sphere(3, 4, 1, 2)
        self.assertEqual(c1, c2)  # förväntas att argumenten är lika

    def test_create_empty_sphere(self):
        with self.assertRaises(ValueError):  # vi förväntar oss att vi testar en Exception (via self.assertRaises) om inte så failar vi
            v = Sphere()

    def test_create_invalid_sphere(self):
        with self.assertRaises(TypeError):
            v = Sphere(5, 1, 2, "a")  # "a")

    def test_two_sphere_not_equal(self) -> None:
        v1 = self.create_sphere()
        v2 = Sphere(4, 2, 5, 4)
        self.assertNotEqual(v1, v2)

    def test_sphere_minus_radius(self) -> None:
        with self.assertRaises(ValueError):
            v = Sphere(-1, 2, 3, 4)


class Lab3Cube(unittest.TestCase):
    def setUp(self) -> None:
        self.side1, self.side2, self.x, self.y, self.z = 4, 4, 3, 4, 2

    def create_cube(self) -> "Cube":
        return Cube(self.side1, self.side2, self.x, self.y, self.z)

    def test_create_cube(self):
        c1 = self.create_cube()
        c2 = Cube(3, 3, 1, 2, 3)
        self.assertEqual(c1, c2)  # förväntas att argumenten är lika

    def test_create_empty_cube(self):
        with self.assertRaises(ValueError):  # vi förväntar oss att vi testar en Exception (via self.assertRaises) om inte så failar vi
            v = Cube()

    def test_create_invalid_cube(self):
        with self.assertRaises(TypeError):
            v = Cube(5, 5, 4, 1, 2)  # "a")

    def test_two_cube_not_equal(self) -> None:
        v1 = self.create_cube()
        v2 = Cube(2, 2, 2, 3, -7)
        self.assertNotEqual(v1, v2)

    def test_cube_minus_lenghts(self) -> None:
        with self.assertRaises(ValueError):
            v = Cube(-1,-1, 3, 2, 7)
"""

# if we run this module directly as main, run the code in the conditional
if __name__ == "__main__":
    unittest.main()  # the code that is ran is unittest.main() which runs all our tests

# the code not ran if imported, because then __name__ is not "__main__"

import unittest
from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube


class Lab3Circle(unittest.TestCase):
    """
    Unit testing for Lab 3
    """
    def setUp(self) -> None:
        self.radius_circle, self.x, self.y = 5, 1, 3

    def create_circle(self) -> "Circle":
        return Circle(self.radius_circle, self.x, self.y)

    # Test start here
    def test_create_circle(self):
        c1 = self.create_circle()
        c2 = Circle(5, 1, 3)
        self.assertEqual(c1, c2)  # expect arguments are equal

    def test_create_empty_circle(self):
        with self.assertRaises(TypeError):  # We except an Exception (via self.assertRaises) unless we fail
            c = Circle()

    def test_create_invalid_circle(self) -> None:
        with self.assertRaises(TypeError):
            c = Circle(5, 1, "a")

    def test_two_circle_not_equal(self) -> None:
        c1 = self.create_circle()
        c2 = Circle(1, 2, 7)
        self.assertNotEqual(c1, c2)

    def test_circle_minus_radius(self) -> None:
        with self.assertRaises(ValueError):
            c = Circle(-1, 2, 7)

    def test_area(self) -> None:
        c1 = self.create_circle()
        self.assertAlmostEqual(c1.circle_areas(), 78.539816339744830961566084581988)


class Lab3Sphere(unittest.TestCase):
    def setUp(self) -> None:
        self.radius_circle, self.x, self.y, self.z = 3, 2, 4, 2

    def create_sphere(self) -> "Sphere":
        return Sphere(self.radius_circle, self.x, self.y, self.z)

    # Test start here
    def test_create_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 4, 2)
        self.assertEqual(s1, s2)  # expect arguments are equal

    def test_create_empty_sphere(self):
        with self.assertRaises(TypeError):  # We except an Exception (via self.assertRaises) unless we fail
            s = Sphere()

    def test_create_invalid_sphere(self):
        with self.assertRaises(TypeError):
            s = Sphere(5, 1, 2, "a")

    def test_two_sphere_not_equal(self) -> None:
        s1 = self.create_sphere()
        s2 = Sphere(4, 2, 5, 4)
        self.assertNotEqual(s1, s2)

    def test_sphere_minus_radius(self) -> None:
        with self.assertRaises(ValueError):
            s = Sphere(-1, 2, 3, 4)

    def test_sphere_volume(self) -> None:
        s1 = self.create_sphere()

    def test_area(self) -> None:
        s1 = self.create_sphere()
        self.assertAlmostEqual(s1.sphere_areas(), 113.09733552923255658465516179806)


class Lab3Rectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.side1, self.side2, self.x, self.y = 4, 3, 4, 6

    def create_rectangle(self) -> "Rectangle":
        return Rectangle(self.side1, self.side2, self.x, self.y)

    # Test start here
    def test_create_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(4, 3, 4, 6)
        self.assertEqual(r1, r2)  # expect arguments are equal

    def test_create_empty_rectangle(self):
        with self.assertRaises(TypeError):  # We except an Exception (via self.assertRaises) unless we fail
            r = Rectangle()

    def test_create_invalid_rectangle(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, 1, "a")

    def test_two_rectangle_not_equal(self) -> None:
        r1 = self.create_rectangle()
        r2 = Rectangle(10, 2, 3, -7)
        self.assertNotEqual(r1, r2)

    def test_rectangle_minus_length(self) -> None:
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 3, 2, 7)

    def test_area(self) -> None:
        r1 = self.create_rectangle()
        self.assertAlmostEqual(r1.rectangle_areas(), 12.0)


class Lab3Cube(unittest.TestCase):
    def setUp(self) -> None:
        self.side1, self.x, self.y, self.z = 4, 3, 4, 2

    def create_cube(self) -> "Cube":
        return Cube(self.side1, self.x, self.y, self.z)

    # Test start here
    def test_create_cube(self):
        c1 = self.create_cube()
        c2 = Cube(4, 3, 4, 2)
        self.assertEqual(c1, c2)  # expect arguments are equal

    def test_create_empty_cube(self):
        with self.assertRaises(TypeError):  # We except an Exception (via self.assertRaises) unless we fail
            c = Cube()

    def test_create_invalid_cube(self):
        with self.assertRaises(TypeError):
            c = Cube(5, 4, 1, "a")

    def test_two_cube_not_equal(self) -> None:
        c1 = self.create_cube()
        c2 = Cube(2, 2, 3, -7)
        self.assertNotEqual(c1, c2)

    def test_cube_minus_length(self) -> None:
        with self.assertRaises(ValueError):
            c = Cube(-1, 3, 2, 7)

    def test_cube_volume(self) -> None:
        c1 = self.create_cube()
        self.assertAlmostEqual(c1.cube_volume(), 64)

    def test_cube_circumradius(self) -> None:
        c1 = self.create_cube()
        self.assertAlmostEqual(c1.cube_circumradius(), 3.4641016151377545870548926830117)


# if we run this module directly as main, run the code in the conditional
if __name__ == "__main__":
    unittest.main()  # the code that is ran is unittest.main() which runs all our tests

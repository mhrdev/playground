import unittest
from triangle import triangle
from nose_parameterized import parameterized

class TestTriangle(unittest.TestCase):

    @parameterized.expand([
        (-1, 5, 6),
        (5, -1, 6),
        (5, 6, -1),
        (0, 5, 6),
        (5, 0, 6),
        (5, 6, 0),
        (-3, -7, -100),
        ])
    def test_invalid_side_length_should_raise_value_error(self, a, b, c):
        with self.assertRaises(ValueError):
            triangle.get_triangle_type(a, b, c)

    @parameterized.expand([
        (None, 5, 6),
        (6, None, 6),
        (6, 5, None),
        ('a', 5, 6),
        (6, 'a', 5),
        (6, 5, 'a'),
        ])
    def test_invalid_side_type_should_raise_value_error(self, a, b, c):
        with self.assertRaises(ValueError):
            triangle.get_triangle_type(a, b, c)

    @parameterized.expand([
        (2, 3, 10),
        (10, 1, 8),
        (4, 10, 2),
        ])
    def test_2_sides_too_short_should_raise_value_error(self, a, b, c):
        with self.assertRaises(ValueError):
            triangle.get_triangle_type(a, b, c)

    @parameterized.expand([
        (5, 5, 5),
        (11.4, 11.4, 11.4),
        (3984.123, 3984.123, 3984.123),
        ])
    def test_equals_sides_triangle_should_return_equilateral_type(self, a, b, c):
        self.assertEquals(triangle.get_triangle_type(a, b, c), triangle.EQUILATERAL)

    @parameterized.expand([
        (5, 5, 5),
        (11.4, 11.4, 11.4),
        (3984.123, 3984.123, 3984.123),
        ])
    def test_all_equals_sides_triangle_should_return_equilateral_type(self, a, b, c):
        self.assertEquals(triangle.get_triangle_type(a, b, c), triangle.EQUILATERAL)

    @parameterized.expand([
        (6, 6, 10),
        (10, 6, 6),
        (6, 10, 6),
        (11.4, 11.4, 0.1),
        ])
    def test_2_equals_sides_triangle_should_return_isosceles_type(self, a, b, c):
        self.assertEquals(triangle.get_triangle_type(a, b, c), triangle.ISOSCELES)

    @parameterized.expand([
        (6, 7, 10),
        (10, 7, 6),
        (7, 10, 6),
        (11.4, 13.4, 3),
        ])
    def test_all_different_sides_triangle_should_return_scalene_type(self, a, b, c):
        self.assertEquals(triangle.get_triangle_type(a, b, c), triangle.SCALENE)

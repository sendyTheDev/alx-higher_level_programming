#!/usr/bin/python3
# test_rectangle.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines tests for models/rectangle.py"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()

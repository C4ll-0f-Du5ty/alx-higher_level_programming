#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with regular lists"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats_in_list(self):
        """Test with lists containing floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([1, 2, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5, -4.5]), -1.5)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 10000000]), 10000000)
        self.assertEqual(max_integer([-1000000, -999999, -10000000]), -999999)

    def test_mixed_types_in_list(self):
        """Test with lists containing mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])

    def test_single_element_list(self):
        """Test with a single-element list"""
        self.assertEqual(max_integer([42]), 42)

    def test_negative_values(self):
        """Test with lists containing negative values"""
        self.assertEqual(max_integer([-10, -5, -8, -3]), -3)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-1, -2, -3, 0]), 0)

    def test_repeated_max_value(self):
        """Test with repeated max values in the list"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-3, -3, -3, -3]), -3)

    def test_list_with_bool_values(self):
        """Test with lists containing boolean values"""
        self.assertEqual(max_integer([True, False, True, False]), True)
        self.assertEqual(max_integer([False, False, False]), False)


if __name__ == '__main__':
    unittest.main()

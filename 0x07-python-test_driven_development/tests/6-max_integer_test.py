#!/usr/bin/python3
"""
Tests for check max integer
into a matrix
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class TestMaxInteger
    """
    def test_max(self):
        """Max value into matrix with integer numbers"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([5, 10, 3, 89]), 89)

    def test_types(self):
        """Make sure type errors are raised when necessary"""
        self.assertRaises(TypeError, max_integer, [1, 2, "Luffy", 4])
        self.assertRaises(TypeError, max_integer, [1, False, True, 4])
        self.assertRaises(TypeError, max_integer, [1, 2, ["Ola k ace"], 4])
        self.assertRaises(TypeError, max_integer, "Monkey D. Luffy")


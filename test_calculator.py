"""Unit tests for the calculator module."""

import unittest

from calculator import add, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    """Test the calculator's arithmetic operations."""

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(8, 0)


if __name__ == "__main__":
    unittest.main()

    def test_decimal_operations(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(divide(1, 4), 0.25)

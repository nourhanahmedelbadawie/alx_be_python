# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for SimpleCalculator class."""

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Normal case
        self.assertEqual(self.calc.add(-1, 1), 0)  # Adding positive and negative
        self.assertEqual(self.calc.add(0, 0), 0)  # Adding zero

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Normal case
        self.assertEqual(self.calc.subtract(0, 5), -5)  # Subtracting a larger number
        self.assertEqual(self.calc.subtract(2, 2), 0)  # Subtracting identical numbers

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)  # Normal case
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Multiplying with a negative number

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)  # Normal case
        self.assertEqual(self.calc.divide(3, 2), 1.5)  # Division resulting in a float
        self.assertEqual(self.calc.divide(0, 5), 0)  # Zero divided by any number
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero returns None

if __name__ == '__main__':
    unittest.main()

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Tests for add ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_signs(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)

    # --- Tests for subtract ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_resulting_in_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # --- Tests for multiply ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(4, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -2), 8)

    def test_multiply_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-4, 2), -8)

    # --- Tests for divide ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_mixed_signs(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_divide_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()

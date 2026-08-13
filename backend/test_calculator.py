import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("add", 10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(calculate("subtract", 10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(calculate("multiply", 10, 5), 50)

    def test_division(self):
        self.assertEqual(calculate("divide", 10, 5), 2)

    def test_decimal_calculation(self):
        self.assertAlmostEqual(calculate("divide", 7, 2), 3.5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("divide", 10, 0)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate("power", 2, 3)


if __name__ == "__main__":
    unittest.main()

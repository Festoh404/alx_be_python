import unittest

from simple_calculator import SimpleCalculator



class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10,30), 40)
    def test_addition(self):
        self.assertEqual(self.calc.add(-20,-5), -25)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(105, 10), 95)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(90, 3), 270)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-3, -7), 21)

    def test_divide(self):
        self.assertEqual(self.calc.divide(32, 8), 4)
    def test_divide(self):
        self.assertEqual(self.calc.divide(35, 0), None)

if __name__ == "__main__":
    unittest.main()
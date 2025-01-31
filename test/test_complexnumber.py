import unittest
import math
from calculator.complexnumber import ComplexNumber  

class TestComplexNumber(unittest.TestCase):
    
    def test_add(self):
        a = ComplexNumber(3, 4)
        b = ComplexNumber(1, 2)
        result = a + b
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imag, 6)

    def test_sub(self):
        a = ComplexNumber(3, 4)
        b = ComplexNumber(1, 2)
        result = a - b
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imag, 2)

    def test_mul(self):
        a = ComplexNumber(3, 4)
        b = ComplexNumber(1, -1)
        result = a * b
        self.assertEqual(result.real, 7)
        self.assertEqual(result.imag, 1)

    def test_div(self):
        a = ComplexNumber(3, 4)
        b = ComplexNumber(1, -1)
        result = a / b
        self.assertAlmostEqual(result.real, -0.5, places=2)
        self.assertAlmostEqual(result.imag, 3.5, places=2)

    def test_absolute_value(self):
        a = ComplexNumber(3, 4)
        result = a.absolute_value()
        self.assertEqual(result, 5)

    def test_argument(self):
        a = ComplexNumber(1, math.sqrt(3))
        result = a.argument()
        self.assertAlmostEqual(result, math.pi / 3, places=2)

    def test_to_polar(self):
        a = ComplexNumber(3, 4)
        r, theta = a.to_polar()
        self.assertAlmostEqual(r, 5, places=2)
        self.assertAlmostEqual(theta, math.atan2(4, 3), places=2)

    def test_to_cartesian(self):
        r = 5
        theta = math.atan2(4, 3)
        result = ComplexNumber.to_cartesian(r, theta)
        self.assertAlmostEqual(result.real, 3, places=2)
        self.assertAlmostEqual(result.imag, 4, places=2)

    def test_square_root(self):
        a = ComplexNumber(3, 4)
        root1, root2 = a.square_root()

        # 제곱근의 제곱이 원래 숫자와 같은지 확인
        result1 = root1 * root1
        result2 = root2 * root2

        self.assertAlmostEqual(result1.real, a.real, places=2)
        self.assertAlmostEqual(result1.imag, a.imag, places=2)
        self.assertAlmostEqual(result2.real, a.real, places=2)
        self.assertAlmostEqual(result2.imag, a.imag, places=2)

    def test_repr(self):
        a = ComplexNumber(3, -4)
        self.assertEqual(repr(a), "3 - 4i")
        b = ComplexNumber(3, 4)
        self.assertEqual(repr(b), "3 + 4i")

if __name__ == "__main__":
    unittest.main()

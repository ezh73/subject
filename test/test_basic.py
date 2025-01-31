import unittest
from calculator.basic import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """각 테스트 전에 실행되는 초기화 메서드"""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(1, 2, 3, 4), 10)
        self.assertEqual(self.calc.add(-1, -2, -3), -6)
        self.assertEqual(self.calc.add(0, 0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 20), -10)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(1, 2, 3, 4), 24)
        self.assertEqual(self.calc.multiply(-1, 2, -3), 6)
        self.assertEqual(self.calc.multiply(5), 5)  # 하나만 넣으면 자기 자신 반환
        self.assertEqual(self.calc.multiply(), 1)  # 아무것도 없으면 기본값 1

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(5, 0), "Cannot divide by zero.")  # 예외 처리 확인

if __name__ == "__main__":
    unittest.main()

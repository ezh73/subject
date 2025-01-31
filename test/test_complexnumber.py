import unittest
from calculator.complexnumber import ComplexNumber
import math

class TestComplexNumber(unittest.TestCase):

    def setUp(self):
        """각 테스트 전에 실행되는 초기화 메서드"""
        self.num1 = ComplexNumber(3, 4)  # 3 + 4i
        self.num2 = ComplexNumber(1, 2)  # 1 + 2i
        self.num_zero = ComplexNumber(0, 0)  # 0 + 0i

    def test_add(self):
        # 덧셈 테스트
        result = self.num1 + self.num2
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imag, 6)

    def test_sub(self):
        # 뺄셈 테스트
        result = self.num1 - self.num2
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imag, 2)

    def test_mul(self):
        # 곱셈 테스트
        result = self.num1 * self.num2
        self.assertEqual(result.real, -5)
        self.assertEqual(result.imag, 10)

    def test_div(self):
        # 나눗셈 테스트
        result = self.num1 / self.num2
        self.assertEqual(round(result.real, 2), 2.2)  # 근사값 비교
        self.assertEqual(round(result.imag, 2), 0.4)

        # 0으로 나누는 경우 예외 처리 테스트
        with self.assertRaises(ValueError):
            self.num1 / self.num_zero

    def test_absolute_value(self):
        # 복소수 절대값 계산 테스트
        result = self.num1.absolute_value()
        self.assertEqual(result, 5)  # sqrt(3^2 + 4^2) == 5

    def test_argument(self):
        # 복소수 편각 계산 테스트
        result = self.num1.argument()
        self.assertEqual(round(result, 2), 0.93)  # atan2(4, 3) 값은 약 0.93 라디안

    def test_to_polar(self):
        # 직교 좌표계 → 극 좌표계 변환 테스트
        result = self.num1.to_polar()
        self.assertEqual(round(result[0], 2), 5)  # 반지름 r == 5
        self.assertEqual(round(result[1], 2), 0.93)  # 각도 θ == 약 0.93 라디안

    def test_to_cartesian(self):
        # 극 좌표계 → 직교 좌표계 변환 테스트
        r, theta = self.num1.to_polar()
        result = ComplexNumber(r, theta).to_cartesian()
        self.assertEqual(round(result.real, 2), 3)  # x == 3
        self.assertEqual(round(result.imag, 2), 4)  # y == 4

    def test_square_root(self):
        # 복소수 제곱근 계산 테스트
        result = self.num1.square_root()
        self.assertEqual(round(result.real, 2), 2)  # 제곱근 실수 부분
        self.assertEqual(round(result.imag, 2), 1)  # 제곱근 허수 부분

    def test_repr(self):
        # 복소수 문자열 출력 형식 테스트
        result = repr(self.num1)
        self.assertEqual(result, "3+4i")

if __name__ == "__main__":
    unittest.main()

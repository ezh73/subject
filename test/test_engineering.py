import unittest
from calculator.engineering import EngineeringCalcultor

class TestEngineeringCalculator(unittest.TestCase):

    def setUp(self):
        """각 테스트 전에 실행되는 초기화 메서드"""
        self.calc = EngineeringCalcultor()

    def test_square_root(self):
        # 제곱근 계산 테스트
        self.assertEqual(self.calc.squre_root(9), 3)
        self.assertEqual(self.calc.squre_root(16), 4)
        self.assertEqual(self.calc.squre_root(25), 5)
        self.assertAlmostEqual(self.calc.squre_root(2), 1.414, places=3)  # 근사값으로 비교

    def test_power(self):
        # 거듭제곱 계산 테스트
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(3, 0), 1)
        self.assertEqual(self.calc.power(7, -1), 1/7)

    def test_log(self):
        # 로그 계산 테스트
        self.assertEqual(self.calc.log(10), 1)  # log10(10) == 1
        self.assertEqual(self.calc.log(100), 2)  # log10(100) == 2
        self.assertEqual(self.calc.log(1000), 3)  # log10(1000) == 3
        with self.assertRaises(ValueError):  # log(0)은 에러 발생해야 함
            self.calc.log(0)

if __name__ == "__main__":
    unittest.main()

import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real  # 실수 부분
        self.imag = imag  # 허수 부분

    # 복소수 사칙연산
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero")
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    # 복소수 절대값 계산
    def absolute_value(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    # 복소수 편각 계산
    def argument(self):
        return math.atan2(self.imag, self.real)
        
    # 직교 좌표계 → 극 좌표계 변환
    def to_polar(self):
        r = self.absolute_value()
        theta = self.argument()
        return (r, theta)  # (반지름, 각도) 튜플 반환
    
    # 극 좌표계 → 직교 좌표계 변환 (수정됨)
    @staticmethod
    def to_cartesian(r, theta):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return ComplexNumber(x, y)

    # 복소수 제곱근 계산 (± 해 포함)
    def square_root(self):
        r = self.absolute_value()
        theta = self.argument()
        sqrt_r = math.sqrt(r)
        sqrt_theta = theta / 2

        root1 = ComplexNumber(sqrt_r * math.cos(sqrt_theta), sqrt_r * math.sin(sqrt_theta))
        root2 = ComplexNumber(-root1.real, -root1.imag)  # 두 번째 해

        return root1, root2

    def __repr__(self):
        return f'{self.real} {"+" if self.imag >= 0 else "-"} {abs(self.imag)}i'

class Calculator:
    def add(self, *args):
        return sum(args)
    
    def subtract(self, a, b):
        return a-b
    
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result
    
    def divide(self,a,b):
        if b == 0:
            return f'Cannot divide by zero.'
        else:
            return a/b
        
import math

class EngineeringCalcultor(Calculator):
    def squre_root(self,x):
        return x**0.5
        #return math.sqrt(x)
    
    def power(self,x,y):
        return x**y
        #return math.pow(x,y) 실수형
    
    def log(self, x):
        return math.log10(x)

    def sin(self, x, angle_unit='radian'):
        if angle_unit == 'degree':
            x = math.radians(x)  # degree를 radian으로 변환
        return math.sin(x)


__all__ = ['Calculator', 'EngineeringCalculator']


if __name__ == '__main__':
    #간단한 데모 코드
    calc = Calculator()
    eng_calc = EngineeringCalcultor()

    print("Basic Calculator Demo:")
    print(calc.add(1,2,3))
    print(calc.multiply(2,4,6))
    print('Engineering Calculator Demo:')
    print(eng_calc.squre_root(16))
    print(eng_calc.sin(30, angle_unit='degree'))

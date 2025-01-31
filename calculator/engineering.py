from .basic import Calculator

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

eng_calc = EngineeringCalcultor()
print(eng_calc.squre_root(16))
print(eng_calc.power(2,3))
print(eng_calc.log(100))

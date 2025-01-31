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
        

calc = Calculator()
print(calc.add(1,2))
print(calc.subtract(10,5))
print(calc.multiply(3,4))
print(calc.divide(5,0))
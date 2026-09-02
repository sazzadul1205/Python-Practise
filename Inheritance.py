class SuperCalculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a
      
      
my_calculator = SuperCalculator()

temp = my_calculator.addition(23, 47)
print(temp)

temp = my_calculator.subtraction(87, 54)
print(temp)

temp = my_calculator.multiplication(65, 56)
print(temp)

temp = my_calculator.division(852, 76)
print(temp)

temp = my_calculator.square(7)
print(temp)

temp = my_calculator.cube(3)
print(temp)


class Calculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

# Here i am inheriting the Calculator class
class SuperCalculator(Calculator):

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a

my_calculator = SuperCalculator()

temp = my_calculator.addition(23, 47)
print(temp)

temp = my_calculator.subtraction(87, 54)
print(temp)

temp = my_calculator.multiplication(65, 56)
print(temp)

temp = my_calculator.division(852, 76)
print(temp)

temp = my_calculator.square(7)
print(temp)

temp = my_calculator.cube(3)
print(temp)

class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError('This is a custom error')
except CustomError as e:
    print(e.message)
    
    
# # Method Overriding
class Calculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

class SuperCalculator(Calculator):

    def addition(self, a, b, c):
        return a + b + c

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a

my_calculator = SuperCalculator()

temp = my_calculator.addition(23, 47, 12)
print(temp)

temp = my_calculator.subtraction(87, 54)
print(temp)

temp = my_calculator.multiplication(65, 56)
print(temp)

temp = my_calculator.division(852, 76)
print(temp)

temp = my_calculator.square(7)
print(temp)

temp = my_calculator.cube(3)
print(temp)

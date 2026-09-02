class WaltonUsta:
    def driving(self):
        print("Walton Usta is driving")

    def music(self):
        print("Walton Usta is playing music")

    def fuel(self):
        print("Walton Usta is refueling")

    def horn(self):
        print("Walton Usta is making a horn noise")
        
car = WaltonUsta()
car.driving()
car.music()
car.fuel()
car.horn()


class Calculator:

    def addition(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a-b

    def multiplication(self, a, b):
        return a*b

    def division(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'
          
          
my_calculator = Calculator()

temp = my_calculator.addition(12, 78)
print(temp)

temp = my_calculator.subtraction(50, 23)
print(temp)

temp = my_calculator.multiplication(9, 19)
print(temp)

temp = my_calculator.division(400, 5)
print(temp)

temp = my_calculator.division(43, 0)
print(temp)

class Calculator:

    # Constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

my_calculator = Calculator(45, 3)

temp = my_calculator.addition()
print(temp)

temp = my_calculator.subtraction()
print(temp)

temp = my_calculator.multiplication()
print(temp)

temp = my_calculator.division()
print(temp)
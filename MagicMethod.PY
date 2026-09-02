class MyClass:
  def __init__(self, a, b):
    self.a = a
    self.b = b
    
    def __del__(self):
      print("Object deleted")
      
class MyClass:

    def __init__(self, var):
        self.var = var

    def __del__(self):
        del self.var

    def __gt__(self, other):
        return len(other) > len(self.var)

    def __lt__(self, other):
        return len(other) < len(self.var)

    def __ge__(self, other):
        return len(other) >= len(self.var)

    def __le__(self, other):
        return len(other) <= len(self.var)
      
a = 5
b = 6

print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(a.__mod__(b))
print(a.__pow__(b))
print(a.__floordiv__(b))


a = a.__float__()
print(type(a))

a = a.__int__()
print(type(a))

a = a.__str__()
print(type(a))

a = a.__repr__()
print(type(a))

a = 'Bangladesh'
b = 'desh'

print(a.__len__())
print(a.__iter__())

print(list(a.__iter__()))

print(a.__contains__(b))
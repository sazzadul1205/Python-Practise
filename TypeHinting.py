def add(a:int, b:int) -> int:
  return a + b

print(type(add(1,2)))

def add(a:int, b:int) -> int:
  print(type(a))
  print(type(b))
  c = a + b
  print(c, type(c))
  return c

print(add(1,2))
print(add('Bangla','Dash'))

# Variable Annotation

# Class and Instance Variable Annotation
from typing import ClassVar

class Human:
    name: str
    age: int
    gender: str
    address: ClassVar[str] = 'Dhaka'

    def __init__(self, name: str = 'sazzadul') -> None:
        self.name = name
        
# Type Variable
from typing import TypeVar

A = TypeVar('A')
B = TypeVar('B', str)
C = TypeVar('C', str, int)

def add(x: A, y: C) -> A:
    pass
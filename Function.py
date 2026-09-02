# Creating functions and making calls

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

def greet_user(username):
    """Display a simple greeting."""
    print("Hello,"+ username+"!")

greet_user("Alice")

def print_my_name(name):
    """Display a simple greeting."""
    print("Hello,"+ name+"!")
    return 

print_my_name("Maateen")

def add(a,b,c):
    return a+b+c

print(add(1,2,3))

# Function parameters or arguments
  # Required argument (Required argument)

def add(a,b):
    return a+b

temp = add(1,2)
print(temp)
# temp = add(1,2,3) # This will raise an error because the function add only takes 2 arguments
# print(temp)

# Keyword argument (keyword argument)
def add(a,b):
    return a+b

temp = add(a=1,b=2)
print(temp)

# Default argument (default argument)
def add(a,b=2):
    return a+b

temp = add(1)
print(temp)

# Variable-length argument
def add(*args):
    print(args)
    print(type(args))
    total = 0
    for i in args:
        total += i
    return total

temp = add(1,2,3,4,5)
print(temp)

def add(**kwargs):
    print(kwargs)
    print(type(kwargs))
    temp = 0
    for key in kwargs:
        temp += kwargs[key]
    return temp

temp = add(a=1,b=2,c=3,d=4,e=5)
print(temp)

# Recursion (Recursion)

# def counter(num):
#     print(num)
#     num += 1
#     counter(num)

# counter(1)


print('Please input a number:')
number = int(input())
temp = number

while number > 1:
    number -= 1
    temp = temp*number

if temp == 0:
    print(1)
else:
    print(temp)
    
# Function of one line: lambda (lambda)
sum = lambda a,b: a+b
print(sum(1,2))


def my_function(func, arg1, arg2):
    return func(arg1, arg2)

print(my_function(lambda a, b : a + b, 10, 20))

# map()
my_list = [2, 3, 4, 5, 6, 7]

def square(num):
    return num**2
  
my_list = list(map(square, my_list))

print(my_list)
print(type(my_list))

# filter()
my_list = [2, 3, 4, 5, 6, 7]

def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False
  
new_list = filter(is_even, my_list)
print(new_list)
print(list(new_list))
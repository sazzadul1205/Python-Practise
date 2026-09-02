# While Loop

# Basic while loop - counting from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

print('The loop has ended.')

# Sum of numbers from 1 to 10 using while loop
print('Sum of 1 to 10')
n = 1
temp = 0
while n <= 10:
    temp += n
    n += 1

print(temp)

# For Loop

# Iterating through a list
a = ['onion', 'potato', 'ginger', 'cucumber']
print(type(a))
for i in a:
    print(i)

# Iterating through a dictionary (iterates over keys)
a = {'name': 'MD. Maksudur Rahman Khan', 'nickname': 'Maateen', 'email': 'maateen@outlook.com', 'phone': '01711223344'}
print(a)
print(type(a))
for i in a:
    print(i)

# Iterating through a string (iterates over characters)
a = 'Python'
for i in a:
    print(i)

# Range function examples

# range(stop)
print(range(10))
print(list(range(5)))  # 0 to 4

# range(start, stop)
print(range(5, 10))
print(list(range(5, 10)))  # 5 to 9

# range(start, stop, step)
print(range(5, 20, 2))
print(list(range(5, 20, 2)))  # 5, 7, 9, 11, 13, 15, 17, 19

# Using range() in for loop
for number in range(1, 11):
    print(number)

# Loop Control Statement

# Break
print('Break statement example')
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# continue
print('Continue statement example')
for i in range(1, 11):
    if i == 5:
        continue
    print(i) 

# pass
print('Pass statement example')
for i in range(1, 11):
    if i == 5:
        pass
    print(i)

# else with loop
print('Else with loop example')

n = 1

while n <= 10:
    print(n)
    n += 1
else:
    print('The loop has ended.')

for n in range(1, 11):
    print(n)
    n += 1
else:
    print('The loop has ended.')

# Infinite Loop

# This will Run a Infinite Loo 
# i = 1
# while i > 0:
#     print(i)
#     i += 1
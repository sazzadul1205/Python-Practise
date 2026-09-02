# Practice
# (1) Use the loop to find the sum of integers from 1 to 100.

print('Sum of 1 to 100')

n = 1
temp = 0
while n <= 100:
    temp += n
    n += 1

print(temp)

# (2) The user will input an integer. Based on that, we will design the triangle of . That is, if the user gives 5 inputs, then I will design a triangle like the following.*

print("Please input the number:")
number = int(input())

for i in range(1, number+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

# (3) A list of at least thirty digits should be made by random selection from the numbers between 1 and 100. This list cannot contain the same number more than once. (If you can't solve it with the knowledge you've gained so far, you'll have to finish the whole book and try again.) )

import random

a = []
while len(a) < 30:
    x = random.randint(1, 100)
    if x not in a:
        a.append(x)

print(a)

# (4) A = {1, 2, 3, 4, 5} and B = {5, 6, 7, 8} are two sets. Instead of using the O function (actually the method), they have to find the union and intersection set C.union()intersection()

A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8}

# Union
print(A | B)

# Intersection
print(A & B)
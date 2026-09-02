# If (if)

a = 5
if a > 0:
    print("a is positive")

# if a < 0:
#     print("a is negative")

# If so... If not... else

a = -5
if a > 0:
    print("a is positive")
else:
    print("a is negative")

# If so... If not... If not... elif … else

a = 0
if a > 0:
    print("a is positive")
elif a < 0:
    print("a is negative")
else:
    print("a is zero")

# Logic when the bird's nest (nested if)

a = int(input("Enter a number: "))
if a > 0:
    print("a is positive")
    if a % 2 == 0:
        print("a is even")
    else:
        print("a is odd")
else:
    print("a is negative or zero")

# Identity vs Equality (is vs ==)

a = [1, 2, 3]

# b refers to the same list object as a
b = a

print(b is a)   # True (same object)
print(b == a)   # True (same values)

# Create a new list containing the same values
b = a[:]

print(b is a)   # False (different objects)
print(b == a)   # True (same values)

a = 4
b = 2 ** 2

print(a is b)   # True (small integers are interned)
print(a == b)   # True (same values)
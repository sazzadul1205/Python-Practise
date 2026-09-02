a = {'orange', 'banana', 'pear', 'apple'}

# get the Value of a
print(a)

# Get the Type of a
print(type(a))

# A = set('orange', 'banana', 'pear', 'apple')

# print(A)

A = set('abracadabra')
print(A)

A = set()
print(type(A))

A = {}
print(type(A))

# Access Items
A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# print(A[0])  # This will raise an error because sets are unordered and do not support indexing

# Add elements
A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("Before Add:", A)

A.add('kiwi')
print("After Add:", A)

A.update(['grape', 'mango'])
print("After Update:", A)

A.update({'berry', 'grape'})
print("After Update:", A)

# Eat the ingredients.
A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("Before Remove:", A)

A.remove('apple')
print("After Remove:", A)

# A.discard('apple')  # This will not raise an error even if 'apple' is not present

A.discard('apple')
print("After Discard:", A)

# A.pop()  # This will raise an error if the set is empty

A.pop()
print("After Pop:", A)

A.clear()
print("After Clear:", A)


A = {1, 2, 3}
B = {3, 4, 5}

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("Difference:", A - B)
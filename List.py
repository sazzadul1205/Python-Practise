a = []

# get the Value of a
print(a)

# Get the Type of a
print(type(a))

# Redeclare a as a list of strings
a = ['onion', 'potato', 'ginger', 'cucumber']

# get the Value of a
print(a)

# Get the Type of a
print(type(a))

# Redeclare a as a list of strings
b = ['onion', 'potato', 'ginger', 'cucumber', 1, 3.1416]

# get the Value of a
print(b)

# Get the Type of a
print(type(b))

##### Access Items #####
print(b[0])
print(b[3])
print(b[1:3])
print(b[:3])
print(b[3:])
print(b[3:])

print(type(b[0]))
print(type(b[3]))
print(type(b[1:3]))
print(type(b[:3]))
print(type(b[3:]))
print(type(b[3:]))

### Update List ###
c = ['onion', 'potato', 'ginger', 'cucumber', 1, 3.1416]
print("Before Update:",c)
c[0] = 'rice'
print("After Update:",c)

# b[6] = 'new'
# print("After Update:",c)

## Append ##
c.append('new')
print("After Append:",c)

## Insert ##
c.insert(1, 'python')
print("After Insert:",c)

## Extends ##
c.extend(['a', 'b', 'c'])
print("After Extends:",c)

## Adding (+) ##
c = c + ['a', 'b', 'c']
print("After Plus:",c)

## Remove Items using del ##
del c[3]
print("After Delete:",c)

## Remove Items using .remove ##
c.remove('python')
print("After Remove:",c)

## Remove Items using .pop ##
c.pop()
print("After POP:",c)

# Check Length
print("Length of the list: ",len(c))

# Get the index of a item
print("Index of Potato :",b.count('potato'))

# Get the Reverse list
c.reverse()
print("Reverse: ", c)

# Create a list of numbers
a = [8, 3, 5, 1, 6, 2, 9, 7, 0, 4]

# Print the list before sorting
print("Before sorting:", a)

# Sort the list in ascending order
a.sort()

# Print the list after sorting
print("After sorting:", a)
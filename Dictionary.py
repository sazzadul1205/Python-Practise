a= {}

print(a)
print(type(a))

a = {'name': 'John', 'age': 30, 'city': 'New York'}
print(a)
print(type(a))

# Access Items
a = {'name': 'John', 'age': 30, 'city': 'New York'}

print(a['name'])
print(a['age'])
print(a['city'])

# Updated Dictionary
a = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Before Update:", a)

a['age'] = 31
print("After Update:", a)

# Add new item
a = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Before Add:", a)

a['country'] = 'USA'
print("After Add:", a)

# Update
a = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Before Update:", a)
b = {'age': 31, 'country': 'USA'}
a.update(b)
print("After Update:", a)


# Remove items, dictionaries
a = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Before Remove:", a)

del a['age']
print("After Remove:", a)

# del a['Country']  # This will raise a KeyError because 'Country' is not a key in the dictionary

# Clear
a = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Before Clear:", a)

a.clear()
print("After Clear:", a)

# Is there or not?
a = {'name': 'John', 'age': 30, 'city': 'New York'}
print('name' in a)  # True
print('country' in a)  # False

# Application of some functions (methods)
a = {'name': 'John', 'age': 30, 'city': 'New York'}

# Copy
b = a.copy()
print("Original Dictionary:", a)
print("Copied Dictionary:", b)

# get(key, default=None)
print(a.get('name'))  # John
print(a.get('country', 'Not Found'))  # Not Found

# items()
print(a.items())

# keys()
print(a.keys())

# values()
print(a.values())
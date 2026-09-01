# Create an empty tuple
a = ()

# Print the tuple
print("Empty tuple:", a)

# Check the type of the tuple
print("Type:", type(a))


# Create a tuple containing vegetables
a = ('onion', 'potato', 'ginger', 'cucumber')

# Print the tuple
print("Tuple:", a)

# Check the type of the tuple
print("Type:", type(a))

# Create a tuple containing different types of items
b = ('onion', 'potato', 'ginger', 'cucumber', 1, 3.1416)

# Access the first item using index 0
print("Item at index 0:", b[0])

# Access the second item using index 1
print("Item at index 1:", b[1])

# Access items from index 1 up to, but not including, index 5
print("Items from index 1 to 4:", b[1:5])

# Access items from the beginning up to, but not including, index 5
print("First 5 items:", b[:5])

# Access items from index 2 to the end
print("Items from index 2:", b[2:])

### Tuple Modification

# Create a tuple
b = ('onion', 'potato', 'ginger', 'cucumber', 1, 3.1416)

# Print the original tuple
print("Before modification:", b)

# Try to change the first item
# This will cause a TypeError because tuples cannot be modified
# b[0] = 'new'

## Counting and Searching 
# Create a tuple with different items
b = ('rice', 'python', 'potato', 343, 'cucumber', 'finger', 23486.4678)

# Find the total number of items in the tuple
print("Number of items:", len(b))

# Count how many times 'potato' appears in the tuple
print("Number of 'potato':", b.count('potato'))


# Create another tuple
c = ('potato', 'a', 'b', 'potato', 'potato')

# Count how many times 'potato' appears
print("Number of 'potato' in c:", c.count('potato'))


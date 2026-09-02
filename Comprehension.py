# List Comprehension

my_list = [i**2 for i in range(20) if i %2 == 0]

print(my_list)

# Set Comprehension
a_list = ['Maateen', 'Khan', 'Maksudur', 'a', 'b', 'c']
my_set = {i for i in a_list if len(i) > 1}

print(my_set)

# Dictionary Comprehension
a_list = ['name', 'country', 'career']
b_list = ['Maateen', 'Bangladesh', 'TeleTalk']

my_dict = {i: j for i, j in zip(a_list, b_list)}

print(my_dict)


# Zip Comprehension
a = [i for i in range(11)]
print(a)

b = [i for i in range(11,21)]
print(b)

c = zip(a, b)

print(list(c))

my_dict = {'career': 'TeleTalk', 'country': 'Bangladesh', 'name': 'Maateen'}

new_dict = {key: value for value, key in my_dict.items()}
print(new_dict)
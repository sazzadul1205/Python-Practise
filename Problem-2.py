# Problem 1
print('Namta of a number')
print('Please input a number:')
number = int(input())

count = 1

while count <= 10:
    print(number, 'x', count, '=', number*count)
    count += 1

# Problem 2
print('Print all numbers from 1 to 100 that are divisible by 3 but not by 5')
my_list = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        my_list.append(i)

print(my_list)

# Problem-3
a = [13, 34, 19, 28, 46, 61, 73, 49, 1, 31, 4, 7, 91, 58, 52, 82, 70, 43, 88, 55, 97, 16, 22, 25, 79, 85, 40, 64, 94, 67, 37]

my_list = []

for i in a:
    if i <= 50:
        my_list.append(i)

print(my_list)

# Problem-4
a = [40, 45, 33, 34, 8, 38, 28, 22, 1, 7, 49, 41, 14, 5, 22, 39, 15, 19, 36, 37, 43, 2, 5, 42, 46, 48, 49, 12, 48, 37, 8, 20, 30, 20, 4, 37, 27, 29, 7, 44, 15, 32, 35, 10, 28, 18, 2, 15, 36, 38]

my_list = []

for i in a:
    if i not in my_list:
        my_list.append(i)

print(my_list)

# Problem-5
print('Please, input the number:')
number = int(input())

temp = number

while temp > 0:
    count = temp
    while count > 0:
        print('*', end='')
        count -= 1
    print()
    temp -= 1

# Problem-6
print('Input your Word:')
word = input()
word = word.casefold()
reverse_word = word[::-1]

if word == reverse_word:
    print('Great its a palindrome!')
else:
    print('Not a palindrome!')

# Problem-7
my_list =  [1, 3, 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56, 65, 77, 94, 100]
print('Please, input the number:')
number = int(input())

first = 0
last = len(my_list) - 1
found = False
cycle = 0

while first <= last and not found:
    midpoint = (first + last) // 2
    if(my_list[midpoint] == number):
        found = True
    else:
        if number < my_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    cycle += 1

print('Number of cycles:', cycle)
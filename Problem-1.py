# Problem 1
print('Check if a number is divisible by 3 and 5')
number = int(input("Enter a number: "))

if number%3 == 0 and number%5 == 0:
    print("yes")
else:
    print("no")

# Problem 2
print('Check if a number is positive, negative or zero')
print('Please, input the number:')
number = float(input())

if number > 0:
    print('The number is positive')
elif number < 0:
    print('The number is negative')
else:
    print('The number is zero')

# Problem 3
print('Check if a number is even or odd')
print('Please, input the number:')
number = int(input())

if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

# Problem 4
print('Check if a character is uppercase or lowercase')
print('Please, input A Character:')
character = input()

if character >= 'A' and character <= 'Z':
    print('The character is uppercase')
elif character >= 'a' and character <= 'z':
    print('The character is lowercase')
else:
    print('The character is neither uppercase nor lowercase')


# Problem-5
print('Check if a character is a vowel or a consonant')
print('Please, input a Character:')
character = input()

if character >= 'a' and character <= 'z' or character >= 'A' and character <= 'Z':
    if character in 'aeiouAEIOU':
        print('The character is a vowel')
    else:
        print('The character is a consonant')
else:
    print('The character is not a letter')


# Problem-6
print('Print the number of notes of 1000, 500, 100, 50, 20, 10, 5 and 1 Taka note(s) of a given amount of Taka.')
a = int(input("Please input your a: "))

b = a
temp = a//1000
print(temp, '1000 Taka note(s).')
if temp > 0:
    a = a%1000
    b = a
else:
    a = b
temp = a//500
print(temp, '500 Taka note(s).')
if temp > 0:
    a = a%500
    b = a
else:
    a = b
temp = a//100
print(temp, '100 Taka note(s).')
if temp > 0:
    a = a%100
    b = a
else:
    a = b
temp = a//50
print(temp, '50 Taka note(s).')
if temp > 0:
    a = a%50
    b = a
else:
    a = b
temp = a//20
print(temp, '20 Taka note(s).')
if temp > 0:
    a = a%20
    b = a
else:
    a = b
temp = a//10
print(temp, '10 Taka note(s).')
if temp > 0:
    a = a%10
    b = a
else:
    a = b
temp = a//5
print(temp, '5 Taka note(s).')
if temp > 0:
    a = a%5
    b = a
else:
    a = b
temp = a//2
print(temp, '2 Taka note(s).')
if temp > 0:
    a = a%2
    b = a
else:
    a = b
temp = a//1
print(temp, '1 Taka note(s).')
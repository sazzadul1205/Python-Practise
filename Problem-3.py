# Problem-1
print("Please input three integers:")
a,b,c = map(int, input().split())

if a > b and a > c:
  greatest = a
elif b > a and b > c:
  greatest = b
else:
  greatest = c
  
print("The greatest number is:", greatest)

# Problem-2
def gcd(a, b):
    if b>a:
      gcd(b, a)
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a
  
print("Please input two integers:")
a,b = map(int, input().split())
print("The GCD of", a, "and", b, "is:", gcd(a,b))


# Problem-3
def gcd(a, b):
    if b > a:
        gcd(b, a)
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

# LCM
def lcm(a, b):
    return (a*b)//gcd(a, b)

print("Please input two integers:")
a, b = map(int, input().split())
print("The LCM of", a, "and", b, "is:", lcm(a, b))

# Problem-4
def is_prime(n):
    if n <= 1:
        raise ValueError('The number must be greater than 1.')
    elif n <= 3:
        return True
    elif (n % 2) == 0 or (n % 3) == 0:
        return False
    else:
        i = 5
        while (i * i) <= n:
            if (n % i) == 0 or (n % (i+2)) == 0:
                return False
            i = i + 6
        return True

print('Please input your number:')
number = int(input())

if is_prime(number):
    print(number, 'is a prime number.')
else:
    print(number, 'is a composite number.')
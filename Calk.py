def swap(c, d):
    c = d + c
    d = c - d
    c = c - d
    
    print("The Swapped Value of C:", c)
    print("The Swapped Value of D:", d)


print("Please Provide the value of C: ")
c = int(input())

print("Please Provide the value of D: ")

d = int(input())

swap(c,d)




print("Value of C:", c)

print("Value of D:", d)
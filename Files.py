# my_file = open("test.txt", "r")
# content = my_file.read()
# print(content)
# my_file.close()

# my_file = open('test.txt', 'r')
# content = my_file.read(5)
# print(content)
# content = my_file.read()
# print(content)
# position = my_file.tell()
# print(position)
# my_file.seek(0, 0)
# content = my_file.read()
# print(content)
# my_file.close()



# 1. READ THE WHOLE FILE
with open("test.txt", "r") as my_file:
    content = my_file.read()
    print(content)


# 2. READ ONLY A SPECIFIC NUMBER OF CHARACTERS
with open("test.txt", "r") as my_file:
    content = my_file.read(5)
    print(content)


# 3. READ THE REST OF THE FILE
with open("test.txt", "r") as my_file:
    content = my_file.read(5)
    print(content)

    content = my_file.read()
    print(content)


# 4. GET THE CURRENT FILE POSITION
with open("test.txt", "r") as my_file:
    content = my_file.read(5)
    print(content)

    position = my_file.tell()
    print(position)


# 5. MOVE THE FILE POSITION USING seek()
with open("test.txt", "r") as my_file:
    content = my_file.read(5)
    print(content)

    my_file.seek(0)

    content = my_file.read()
    print(content)


# 6. READ THE FILE LINE BY LINE
with open("test.txt", "r") as my_file:
    for line in my_file:
        print(line)


# 7. READ THE FILE LINE BY LINE WITHOUT EXTRA BLANK LINES
with open("test.txt", "r") as my_file:
    for line in my_file:
        print(line.strip())


# 8. READ ALL LINES INTO A LIST
with open("test.txt", "r") as my_file:
    lines = my_file.readlines()

print(lines)


# 9. WRITE TO A FILE
with open("test.txt", "w") as my_file:
    my_file.write("Hello Python")


# 10. WRITE MULTIPLE LINES
with open("test.txt", "w") as my_file:
    my_file.write("Hello\n")
    my_file.write("Python\n")
    my_file.write("Programming\n")


# 11. APPEND TO A FILE
with open("test.txt", "a") as my_file:
    my_file.write("\nNew line")


# 12. READ AND WRITE USING r+
with open("test.txt", "r+") as my_file:
    content = my_file.read()
    print(content)

    my_file.write("\nNew content")



# 15. RECOMMENDED WAY: WITH
with open("test.txt", "r") as my_file:
    content = my_file.read()
    print(content)

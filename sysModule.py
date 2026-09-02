import sys


# sys.argv
print("Command-line arguments:")
print(sys.argv)

for arg in sys.argv:
    print(arg)


# sys.exc_info()
try:
    print(10 / 0)
except ZeroDivisionError:
    print("\nException information:")
    print(sys.exc_info())


# sys.executable
print("\nPython executable:")
print(sys.executable)


# sys.path
print("\nPython module search paths:")
for path in sys.path:
    print(path)


# sys.platform
print("\nOperating system platform:")
print(sys.platform)
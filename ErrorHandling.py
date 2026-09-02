# try … except#
try:
  with open("test2.txt", "r") as my_file:
    content = my_file.read()
    print(content)
except FileNotFoundError:
  print("File not found. Please check the file path.")
  
  try:
    with open("test2.txt", "r") as my_file:
      content = my_file.read()
      print(content)
  except FileNotFoundError:
    print("File not found. Please check the file path.")


try:
  my_list = []
  print(my_list[0])
except IndexError:
  print("Index out of range.")
  
try:
  my_file = open("test.txt", "r")
  content = my_file.read()
  i = int(content.strip())
  
except IOError as e:
  errno, strerror = e.args
  print("I/O error({0}): {1}".format(errno, strerror))
  
except ValueError:
  print("No Valid Integer in the file.")
  
except:
  print("Something went wrong.")
  
try:
    my_file = open('test2.txt')
    content = my_file.read()
    i = int(content.strip())

except (IOError, ValueError):
    pass

# try … except … else
try: 
  a = 10
  b = 8
  print(a/b)
  
except ValueError as e: 
  print(e)
  
else: 
  print("No error")
  
# try … except … finally
try:
  with open("test2.txt", "r") as my_file:
    content = my_file.read()
    print(content)

except FileNotFoundError:
  print("File not found. Please check the file path.")

finally:
  print("The 'try except' is finished.")
  
# Raise Exception
try:
  raise NameError("This is an exception")

except NameError as e:
  print(e)
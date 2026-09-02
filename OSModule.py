import os


# os.getcwd()
print("Current working directory:")
print(os.getcwd())


# os.chdir()
os.chdir(r"G:\python project")
print("\nChanged working directory:")
print(os.getcwd())


# os.mkdir()
# os.mkdir("new_folder")
# print("\nDirectory created: new_folder")


# os.makedirs()
# os.makedirs("folder1/folder2/folder3")
# print("\nNested directories created.")


# os.remove()
# os.remove("test.txt")
# print("\nFile removed: test.txt")


# os.rmdir()
# os.rmdir("new_folder")
# print("\nDirectory removed: new_folder")


# os.rename()
# os.rename("old.txt", "new.txt")
# print("\nFile renamed: old.txt -> new.txt")


# os.path.basename()
path = r"G:\python project\Python-Practise\test.py"

print("\nFile name:")
print(os.path.basename(path))


# os.path.dirname()
print("\nDirectory name:")
print(os.path.dirname(path))


# os.path.exists()
print("\nPath exists:")
print(os.path.exists(path))


# os.path.isdir()
print("\nIs directory:")
print(os.path.isdir(path))


# os.path.isfile()
print("\nIs file:")
print(os.path.isfile(path))


# os.path.join()
directory = os.getcwd()
file_path = os.path.join(directory, "test.py")

print("\nJoined path:")
print(file_path)


# os.path.split()
print("\nSplit path:")
print(os.path.split(path))


# os.system()
# os.system("dir")  # Windows
# os.system("ls")   # Linux/macOS
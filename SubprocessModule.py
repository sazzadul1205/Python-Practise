import shlex
import subprocess


# run()
# output = subprocess.run(["ls", "-l"])  # Linux
output = subprocess.run(["cmd", "/c", "dir"])  # Windows

print(output)


# Capture command output
# output = subprocess.run(
#     ["cmd", "/c", "dir"],
#     stdout=subprocess.PIPE
# )

# print(type(output))
# print(output)
# print(type(output.stdout))

# result = output.stdout.decode("UTF-8")
# print(result)


# System information
# output = subprocess.run(["uname"])  # Linux
output = subprocess.run(["cmd", "/c", "ver"])  # Windows

print(output)


# Detailed system information
# output = subprocess.run(["uname", "-r"])  # Linux
output = subprocess.run(["cmd", "/c", "systeminfo"])  # Windows

print(output)


# Popen()
# output = subprocess.Popen(["cmd", "/c", "systeminfo"])
# print(type(output))
# print(output)


# shlex.split()
# command = "cmd /c systeminfo"
# args = shlex.split(command)

# print(args)

# output = subprocess.Popen(args)
# print(output)


# call()
# output = subprocess.call(["cmd", "/c", "dir"])
# print(output)


# Return code
output = subprocess.call(["cmd", "/c", "dir"])

print("\nReturn code:")
print(output)
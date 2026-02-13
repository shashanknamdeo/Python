"""

| Mode  | Meaning                 |
| ----- | ----------------------- |
|  "r"  | Read (default)          |
|  "w"  | Write (overwrites file) |
|  "a"  | Append (adds to file)   |
|  "x"  | Create new file         |
|  "b"  | Binary mode             |
|  "+"  | Read and Write          |

"""

# Access a file and perform file operation in Python

file = open("filename.txt", "mode")


# Read
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Write
file = open("data.txt", "w")
file.write("Hello Shashank\n")
file.write("Learning Python File Handling")
file.close()


# Best practice to use 'with'. This automatically closes the file.

# ex:

with open("Filename.txt", "mode") as file:

# Read
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Write
with open("data.txt", "w") as file:
    file.write("Python is powerful")

file.read()         # Reads entire file as a single string, Returns → String, Used when file is small
file.readline()     # Reads one line at a time, Returns → String, Cursor moves to next line after each call
file.readlines()    # Reads all lines, Returns → List of strings

file.write("Hello\n")                       # Writes single string, Returns number of characters written
file.writelines(["Hello\n", "Python\n"])    # Writes list of strings, Does NOT automatically add \n
print("File input and output in Python")
print("File input and output (I/O) in Python allows you to read from and write to files. It is an essential part of many applications, enabling data persistence and manipulation.")

print("File input format is 'with open(filename, mode) as file:' where 'filename' is the name of the file and 'mode' specifies the operation (e.g., 'r' for reading, 'w' for writing).")
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("File I/O in Python is straightforward and easy to use.\n")
print("Data has been written to 'example.txt'.")

print("File output format is 'with open(filename, mode) as file:' where 'filename' is the name of the file and 'mode' specifies the operation (e.g., 'r' for reading, 'w' for writing).")
# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
print("Content of 'example.txt':")
print(content)

print("'r' mode is used for reading files,\n'w' mode is used for writing files (overwrites existing content), and \n'a' mode is used for appending to files (adds content to the end of the file).\n'x' mode is used for creating a new file and writing to it (fails if the file already exists).\n'b' mode is used for binary files, and \n't' mode is used for text files (default mode).\n'+' mode is used for updating (reading and writing) files.")

with open("example.txt", "a") as file:
    file.write("This line is appended to the file.\n")
print("Data has been appended to 'example.txt'.")
with open("example.txt", "r") as file:
    content = file.read()
print("Updated content of 'example.txt':")
print(content)

import os
os.remove("example.txt")
print("File 'example.txt' has been deleted using os.remove().")

with open("example.txt", "x") as file:
    file.write("This is a new file created using 'x' mode.\n")
print("A new file 'example.txt' has been created using 'x' mode.")
with open("example.txt", "b") as file:
    file.write(b"This is a binary file.\n")
print("A binary file 'example.txt' has been created using 'b' mode.")
with open("example.txt", "t") as file:
    file.write("This is a text file.\n")
print("A text file 'example.txt' has been created using 't' mode.")
with open("example.txt", "r+") as file:
    content = file.read()
    file.write("This line is added to the file using 'r+' mode.\n")
print("Data has been added to 'example.txt' using 'r+' mode.")

print("Opening and Closing Files: In Python, files are opened using the 'open()' function and closed using the 'close()' method. However, it is recommended to use the 'with' statement to open files, as it automatically takes care of closing the file after the block of code is executed.")
open_file = open("example.txt", "r")
print("File 'example.txt' is opened.")
open_file.close()
print("File 'example.txt' is closed.")

print("Deleting a file using os module: You can delete a file using the 'os' module in Python. The 'os.remove()' function is used to delete a file.")


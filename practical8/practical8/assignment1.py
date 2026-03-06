# Construct a program that reads a text file and writes its contents into a new text file with the same content but in uppercase.

source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

with open(source_file, "r") as file1:
    content = file1.read()

upper_content = content.upper()

with open(destination_file, "w") as file2:
    file2.write(upper_content)

print("Content copied in uppercase successfully.")
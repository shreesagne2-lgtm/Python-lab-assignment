# Develop an application using file handling to copy the contents of python script into another without including the comments.

source_file = input("Enter source python file name: ")
destination_file = input("Enter destination file name: ")

with open(source_file, "r") as file1:
    lines = file1.readlines()

with open(destination_file, "w") as file2:
    for line in lines:
        if not line.strip().startswith("#"):
            file2.write(line)

print("\nSource File Content:")
with open(source_file, "r") as f:
    print(f.read())

print("\nDestination File Content (without comments):")
with open(destination_file, "r") as f:
    print(f.read())
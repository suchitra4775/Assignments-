import os


file_name = input("Enter the file name:")

if os.path.isfile(file_name):
    print(f"File '{file_name}' file exists")
else:  
    print(f"File '{file_name}' file does not exist")


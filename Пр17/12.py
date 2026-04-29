import os

file_name = 'data.txt'
if os.path.exists(file_name):
    print(f"The file'{file_name}' exists.")
else:
    print(f"The file '{file_name}' does not exist.")

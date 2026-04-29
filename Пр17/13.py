import os

file_name = 'data.txt'

if os.path.exists(file_name):
    file_size = os.path.getsize(file_name)
    print(f"File size '{file_name}': {file_size} bite.")
else:
    print(f"File '{file_name}' not found.")

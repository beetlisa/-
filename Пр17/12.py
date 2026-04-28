import os

file_name = 'data.txt'
if os.path.exists(file_name):
    print(f"Файл '{file_name}' существует.")
else:
    print(f"Файл '{file_name}' не существует.")
import os

file_name = 'data.txt'

if os.path.exists(file_name):
    file_size = os.path.getsize(file_name)
    print(f"Размер файла '{file_name}': {file_size} байт.")
else:
    print(f"Файл '{file_name}' не найден.")
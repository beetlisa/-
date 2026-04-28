import json

my_dict = {
    "name": "Alice",
    "age": 19,
    "is_student": False,
}

file_name = "data.json"

with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False, indent=4)

print(f"Словарь успешно сохранен в файл '{file_name}'.")
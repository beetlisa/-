import json

file_name = "data.json"

with open(file_name, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print("File Contents 'data.json':")
print(loaded_data)

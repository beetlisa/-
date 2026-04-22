import re

text19 = "Name: John Age: 25"
name_match = re.search(r'Name:\s+(\w+)', text19)
age_match = re.search(r'Age:\s+(\d+)', text19)
if name_match and age_match:
    print(f"Имя: {name_match.group(1)}, Возраст: {age_match.group(1)}")
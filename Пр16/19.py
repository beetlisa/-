import re

text19 = "Name: John Age: 25"
name_match = re.search(r'Name:\s+(\w+)', text19)
age_match = re.search(r'Age:\s+(\d+)', text19)
if name_match and age_match:
    print(f"Name: {name_match.group(1)}, Age: {age_match.group(1)}")

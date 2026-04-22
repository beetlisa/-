import re

text15 = "hello world python programming"
result15 = re.sub(r'\b\w', lambda m: m.group(0).upper(), text15)
print(result15)
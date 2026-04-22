import re

text14 = "hello hello world"
result14 = re.findall(r'\b(\w+)\s+\1\b', text14)
print(result14)
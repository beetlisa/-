import re

text12 = "<p>Hello</p>"
result12 = re.sub(r'<[^>]+>', '', text12)
print(result12)
import re

text1 = "I love Python programming"
result1 = bool(re.search(r'Python', text1))
print(result1)
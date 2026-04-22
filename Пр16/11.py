import re

text11 = "a b c hello python hi"
result11 = re.sub(r'\b\w{1,3}\b', '****', text11)
print(result11)
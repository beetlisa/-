import re

text2 = "There are 12 apples and 5 bananas"
result2 = re.findall(r'\d+', text2)
print(result2)
import re

text5 = "abc123def45"
result5 = re.sub(r'\d', '', text5)
print(result5)
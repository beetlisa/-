import re

text6 = "Apple and banana are amazing"
result6 = re.findall(r'\b[Aa][a-zA-Z]*\b', text6)
print(result6)
import re

text10 = "apple, banana orange,grape"
result10 = re.split(r'[,\s]+', text10.strip())
print(result10)
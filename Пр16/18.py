import re

card_number = "1234 5678 9012 3456"
result18 = re.sub(r'\d(?=.{5,})', '*', card_number)
print(result18)
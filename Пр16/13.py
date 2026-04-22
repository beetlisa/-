import re

text13 = "Visit https://example.com and http://test.org"
result13 = re.findall(r'https?://[a-zA-Z0-9./-]+', text13)
print(result13)
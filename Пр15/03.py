import re

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
clean_text = re.sub(r'[^\w\s]', '', text)
with open('clean.txt', 'w', encoding='utf-8') as f:
    f.write(clean_text)
import re

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
words = re.findall(r'\b\w+\b', text.lower())
unique_count = len(set(words))
print(f"Количество уникальных слов: {unique_count}")
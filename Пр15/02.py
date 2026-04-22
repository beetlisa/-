import re
from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
word_counts = Counter(words)
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")
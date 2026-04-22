import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open('filtered.csv', 'w', encoding='utf-8') as f:
    f.write(lines[0]) # заголовок
    for line in lines[1:]:
        age = int(line.strip().split(',')[1])
        if age > 25:
            f.write(line)
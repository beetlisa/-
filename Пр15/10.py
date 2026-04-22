with open('input.txt', 'r', encoding='utf-8') as f:
    unique_lines = set(f.readlines())
with open('unique_lines.txt', 'w', encoding='utf-8') as f:
    f.writelines(unique_lines)
print("”никальные строки записаны в unique_lines.txt")
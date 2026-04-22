with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
longest = max(lines, key=len)
print(f"Длина: {len(longest)}\nСтрока: {longest.strip()}")
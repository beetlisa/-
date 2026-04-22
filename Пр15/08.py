with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
capital_start = sum(1 for line in lines if line and line[0].isupper())
print(f"Строк, начинающихся с заглавной буквы: {capital_start}")
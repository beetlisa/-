import random
from datetime import datetime
import os

filename = "numbers.txt"

# генерация чисел
numbers = [random.randint(1, 100) for _ in range(5)]

# запись
with open(filename, "w") as f:
    f.write(f"Дата: {datetime.now()}\n")
    f.write("Числа: " + " ".join(map(str, numbers)))

# проверка файла
print("Файл существует:", os.path.exists(filename))

# чтение
with open(filename, "r") as f:
    print(f.read())
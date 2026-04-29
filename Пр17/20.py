import random
from datetime import datetime
import os

filename = "numbers.txt"

numbers = [random.randint(1, 100) for _ in range(5)]

with open(filename, "w") as f:
    f.write(f"Date: {datetime.now()}\n")
    f.write("Number: " + " ".join(map(str, numbers)))

print("File exists:", os.path.exists(filename))

with open(filename, "r") as f:
    print(f.read())

from datetime import datetime
from collections import Counter
import re

error_by_day = {}
with open('log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if "ERROR" in line:
            date_part = line.split()[0] # первое слово Ч дата
            error_by_day[date_part] = error_by_day.get(date_part, 0) + 1

for day, count in sorted(error_by_day.items()):
    print(f"{day}: {count}")
import re

log_line = "2026-04-01 ERROR Something failed"
match = re.search(r'(\d{4}-\d{2}-\d{2})\s+(INFO|ERROR)\s+(.+)', log_line)
if match:
    print(f"Дата: {match.group(1)}")
    print(f"Уровень: {match.group(2)}")
    print(f"Сообщение: {match.group(3)}")
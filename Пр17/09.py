import datetime

date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 1, 31)

delta = date2 - date1

print(f"Разница между {date1} и {date2} составляет {delta.days} дней.")
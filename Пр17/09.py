import datetime

date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 1, 31)

delta = date2 - date1

print(f"Difference between {date1} and {date2} amounts to {delta.days} days.")

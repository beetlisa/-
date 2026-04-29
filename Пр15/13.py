from datetime import timedelta
from datetime import date

given_date = date(2024, 12, 31)
days_ahead = 0 - given_date.weekday()
if days_ahead <= 0:
    days_ahead += 7
next_monday = given_date + timedelta(days=days_ahead)
print(f"Next Monday: {next_monday}")

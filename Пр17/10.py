import datetime

current_date = datetime.date.today()
future_date = current_date + datetime.timedelta(days=7)

print(f"Current date: {current_date}")
print(f"Date in 7 days: {future_date}")

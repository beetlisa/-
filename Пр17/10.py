import datetime

current_date = datetime.date.today()
future_date = current_date + datetime.timedelta(days=7)

print(f"Текущая дата: {current_date}")
print(f"Дата через 7 дней: {future_date}")
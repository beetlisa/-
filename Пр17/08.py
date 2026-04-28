import datetime

current_date = datetime.date.today()
formatted_date = current_date.strftime("%Y-%m-%d")
print(f"Текущая дата в формате YYYY-MM-DD: {formatted_date}")
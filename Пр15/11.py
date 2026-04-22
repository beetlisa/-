from datetime import datetime

date_obj = datetime.strptime("2024-12-31", "%Y-%m-%d")
print(f"День: {date_obj.day}, Месяц: {date_obj.month}, Год: {date_obj.year}")
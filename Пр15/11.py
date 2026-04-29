from datetime import datetime

date_obj = datetime.strptime("2024-12-31", "%Y-%m-%d")
print(f"Day: {date_obj.day}, month: {date_obj.month}, year: {date_obj.year}")

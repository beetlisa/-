from datetime import datetime

birth = datetime.strptime(input("enter date of birth (YYYY-MM-DD): "), "%Y-%m-%d")
age_days = (datetime.now() - birth).days
print(f"Age in days: {age_days}")

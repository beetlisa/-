from datetime import datetime

birth = datetime.strptime(input("Введите дату рождения (ГГГГ-ММ-ДД): "), "%Y-%m-%d")
age_days = (datetime.now() - birth).days
print(f"Возраст в днях: {age_days}")
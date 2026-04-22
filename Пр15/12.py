from datetime import timedelta
from datetime import date

def workdays_between(start_date, end_date):
    delta = end_date - start_date
    workdays = 0
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        if day.weekday() < 5: # 0=пн, 4=пт, 5=сб, 6=вс
            workdays += 1
    return workdays

start = date(2024, 12, 1)
end = date(2024, 12, 31)
print(f"Рабочих дней: {workdays_between(start, end)}")
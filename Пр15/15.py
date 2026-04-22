date_strings = ["2024-12-31", "2023-01-15", "2024-06-01"]
sorted_dates = sorted(date_strings, key=lambda x: datetime.strptime(x, "%Y-%m-%d"))
print(sorted_dates)
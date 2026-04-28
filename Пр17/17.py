import csv
users = [
    ["Name", "Age"],
    ["Alice", 19],
    ["Kseniya", 18]
]

with open("users.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerows(users)
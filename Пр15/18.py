from datetime import datetime

deadline = datetime(2026, 4, 10)
if datetime.now() > deadline:
    print("deadline is overdue")
else:
    print("the deadline has not arrived yet")

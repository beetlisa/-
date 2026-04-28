import random
from datetime import datetime, timedelta

start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)

random_date = start + timedelta(days=random.randint(0, 364))
print(random_date)
import re
from collections import Counter

log_text = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""

error_by_date = Counter()
for line in log_text.split('\n'):
    if 'ERROR' in line:
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', line)
        if date_match:
            error_by_date[date_match.group(1)] += 1

for date, count in sorted(error_by_date.items()):
    print(f"{date}: {count}")
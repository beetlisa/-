from datetime import datetime

with open('log_messages.txt', 'a', encoding='utf-8') as f:
    msg = input("enter message: ")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    f.write(f"{timestamp} {msg}\n")
print("message added to log_messages.txt")

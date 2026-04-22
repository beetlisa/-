from datetime import datetime

with open('log_messages.txt', 'a', encoding='utf-8') as f:
    msg = input("¬ведите сообщение: ")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    f.write(f"{timestamp} {msg}\n")
print("—ообщение добавлено в log_messages.txt")
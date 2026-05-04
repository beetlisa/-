import threading
import time

def daemon_task():
    while True:
        print("Daemon running...")
        time.sleep(2)

t = threading.Thread(target=daemon_task, daemon=True)
t.start()

time.sleep(5)
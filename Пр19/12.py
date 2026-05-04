import threading
import time

def io_task():
    time.sleep(1)
    print("Loaded")

threads = [threading.Thread(target=io_task) for _ in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()
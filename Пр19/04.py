import threading
import time

def delayed():
    for i in range(3):
        time.sleep(1)
        print(f"Delayed {i}")

threading.Thread(target=delayed).start()
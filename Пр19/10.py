import threading
from multiprocessing import Process
import time

def heavy():
    sum(range(10_000_000))

# threading
start = time.time()

threads = [threading.Thread(target=heavy) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Threading:", time.time() - start)

# multiprocessing
start = time.time()

processes = [Process(target=heavy) for _ in range(2)]
for p in processes:
    p.start()
for p in processes:
    p.join()

print("Multiprocessing:", time.time() - start)
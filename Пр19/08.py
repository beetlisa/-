import threading
import queue

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"Processing {item}")
        q.task_done()

q = queue.Queue()

for i in range(10):
    q.put(i)

for _ in range(3):
    threading.Thread(target=worker, args=(q,)).start()

q.join()
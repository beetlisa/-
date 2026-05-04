from multiprocessing import Process

def cpu_task():
    total = 0
    for i in range(10000000):
        total += i

processes = [Process(target=cpu_task) for _ in range(2)]

for p in processes:
    p.start()

for p in processes:
    p.join()
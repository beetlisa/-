from multiprocessing import Process

def calc_sum():
    print(sum(range(1, 100001)))

p1 = Process(target=calc_sum)
p2 = Process(target=calc_sum)

p1.start()
p2.start()

p1.join()
p2.join()
import asyncio

async def producer(q):
    for i in range(5):
        await q.put(i)
        print("Produced", i)

async def consumer(q):
    while True:
        item = await q.get()
        print("Consumed", item)
        q.task_done()

async def main():
    q = asyncio.Queue()

    asyncio.create_task(consumer(q))
    await producer(q)
    await q.join()

asyncio.run(main())
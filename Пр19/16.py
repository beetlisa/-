import asyncio

async def task(n):
    await asyncio.sleep(1)
    print(f"Task {n}")

asyncio.run(asyncio.gather(task(1), task(2), task(3)))
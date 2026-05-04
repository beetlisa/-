import asyncio

async def task():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(task())
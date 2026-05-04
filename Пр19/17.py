import asyncio

async def task(n, delay):
    await asyncio.sleep(delay)
    print(f"Finished {n}")

async def main():
    await asyncio.gather(
        task(1, 3),
        task(2, 1),
        task(3, 2),
    )

asyncio.run(main())
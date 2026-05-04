import asyncio

async def read(name):
    await asyncio.sleep(1)
    print(f"Read {name}")

async def main():
    await asyncio.gather(read("file1"), read("file2"))

asyncio.run(main())
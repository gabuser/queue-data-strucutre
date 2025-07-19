import asyncio 

queues = asyncio.Queue()
numbers =[c for c in range(0,10)]

async def worker(lenght:int):
    for c in range(0, len(numbers),lenght):
        await asyncio.sleep(2)
        yield numbers[c:c+lenght]
    
async def geting():
    async for a in worker(2):
        for b in a:
            await queues.put(b)

async def showing():
    for c in range(len(numbers)):
        data =await queues.get()

        print(data)

async def main():
    await asyncio.gather(geting(),showing())

asyncio.run(main())
"""for c in worker(4):
    print(c)"""
"""async def getting():
    async for toget in worker():"""


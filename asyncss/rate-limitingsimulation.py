import asyncio 

queues = asyncio.Queue()

async def attackr(package = 'package'):
    while True:
        try:
            await asyncio.sleep(1)
            await queues.put(package)
        
        except KeyboardInterrupt:
            await queues.put(None)

async def reciver():
    while True:

        data = await queues.get()
        
        if(data is None):
            break

        print(data)

async def main():
    await asyncio.gather(attackr(), reciver())

asyncio.run(main())
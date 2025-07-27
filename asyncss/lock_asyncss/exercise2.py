import asyncio 
import random 

queues = asyncio.Queue()
locks = asyncio.Lock()
chosed = 0

async def producer():
    for _ in range(10):
        randomized = random.randint(0,100)
        await queues.put(randomized)

async def consumer():
    global chosed
    #chosed = 0
    while True:
        #async with locks:
            returned = await queues.get()

            print(returned)

            async with locks:
                chosed+=1
                print(f'executed tasks: {chosed}')
            if(returned is None):
                break
    
    print(queues.qsize())

async def main():
    producers = []
    consumers =[]

    for _ in range(0,3):
        producers.append(producer())
    
    for _ in range(0,2):
        consumers.append(consumer())

    await asyncio.gather(*producers)

    if(queues.qsize() == 30):
         for _ in range(2):
            await queues.put(None)
    await asyncio.gather(*consumers)
   

asyncio.run(main())
    
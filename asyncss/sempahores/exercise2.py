import asyncio 
import random 
import aiofiles

queues = asyncio.Queue()
queues2 = asyncio.Queue()
locking = asyncio.Lock()
semaphore = asyncio.Semaphore(2)
runner = False
failed = []
counter = 0

async def files():
    async with aiofiles.open("url.txt",'r') as r:
        datas = await r.read()
        datas= iter(datas.split("\n"))
    return datas


async def producer(values,semaphore:object):
    #global falied

    while True:
        #await asyncio.sleep(random.randint(1,2))
        
        try:
            async with semaphore:
                data = next(values)
                await queues.put(data)
                await asyncio.sleep(random.randint(1,2))
        except StopIteration:
            #for _ in range(0):
            await queues.put(None)
            break

async def consumer(semaphore):
    global counter,runner

    while True:
        async with semaphore:
            recived = await queues.get()

            if(recived is None):
                break

            else:
                await queues2.put(recived)

                async with locking:
                    counter+=1 
            
                if(counter == 20):
                    #print(True)
                    #for _ in range(2):
                        await queues2.put(None)
        
        print('rodando')
async def showing():

    while True:
        donwloaded = await queues2.get()
        print(donwloaded)
        if(donwloaded is not None):
            print(f"donwloaded sites {donwloaded}")
            #pass
        
        else:
            failed = queues.qsize
            print(f' has failed to donwload:{failed}')
            break

async def main():
    global runner, failed

    producers = []
    consumers = []

    filess = await files()
    try:
        for _ in range(4):
            producers.append(asyncio.wait_for(producer(filess,semaphore),timeout=10))
        
        for __ in range(2):
            consumers.append(consumer(semaphore))
    
        await asyncio.gather(*producers, *consumers, showing())

        #for ___ in range(2):
         #   await queues.put(None)

        #await asyncio.gather(*consumers)

        #show = showing()
        #await show
        
    except asyncio.TimeoutError:
        print(True)

        await queues2.put(None)

asyncio.run(main())
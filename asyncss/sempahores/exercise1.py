import asyncio 
import aiofiles

semaphore = asyncio.Semaphore(3)
queues = asyncio.Queue()
queues2 = asyncio.Queue()
locks = asyncio.Lock()

counter = 0
lists = []

async def files():
    async with aiofiles.open("ips.txt") as file:
        getting = await file.read()
        values = iter(getting.split('\n'))
        #queues.put(getting)
        return values

async def producer(lenght, ids:str,semaphores:object):
    
    while(True):
        try:
            print(f'\n worker {ids} is now working')
            async with semaphores:
                datas = next(lenght)
                await queues.put(datas)
                #print(f'\n working {ids} ')
        
        except StopIteration:
            #print(True)
            break

async def consumers(semaphores:object):
    global counter

    while True:
        async with semaphores:
            recived = await queues.get()

            if(recived is None):
                #await queues2.put(None)
                break

            else:

                async with locks:
                    counter+=1 

                await queues2.put(recived)
                
                if(counter == 20):
                    #counter+=1
                    await queues2.put(None)
            
            #await queues2.put(recived)

async def outputing():
    global counter

    while True:
        writing = await queues2.get()
        #print(writing)
        
        if(writing is None):
            break
            #lists.append(writing)
        
        async with aiofiles.open("output.txt",'a') as file:
            await file.write(writing+"\n")

    print(queues2.qsize())

async def main():
    workers = []
    consumer = []
    
    returned = await files()

    print(type(returned))
    for ids in range(5):
        workers.append(producer(returned, ids, semaphore))
    

    await asyncio.gather(*workers)
    for _ in range(4):
        await queues.put(None)
    
    #await queues2.put(None)

    for consuming in range(4):
        consumer.append(consumers(semaphore))
    
    await asyncio.gather(*consumer)
    
    task3 = outputing()
    await task3

asyncio.run(main())



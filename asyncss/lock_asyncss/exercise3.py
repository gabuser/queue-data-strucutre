import asyncio
import random

queues = asyncio.Queue()
lokcs = asyncio.Lock()
tasks = 0

def fun():
    with open('fakesites.txt','r') as log:
        logs = iter(log.read().split("\n"))
        for _ in logs:
            yield _

datasloaded= fun()

async def donwloading(datas:str):
    while True:
        try:
            #print(f'\n downloading {datas}')
            await asyncio.sleep(random.randint(0,3))
            async with lokcs:
                values = next(datas)
            
            print(f'downloading {values}')
            await queues.put(values)

            #await asyncio.sleep(random.randint(0,3))
            #print('\n downloaded')
        
        except StopIteration:
            break

async def donwloaded():
    global tasks
    #while True:
    
    for _ in range(15):
        data = await queues.get()

        print(f'\n site: {data} has been downloaded')

        async with lokcs:
            tasks+=1 
            print(f'\n tasks executed {tasks}')
    
    print(queues.qsize())

async def main():
    producers = []
    consumers = []

    for _ in range(5):
        producers.append(donwloading(datasloaded))
        
    await asyncio.gather(*producers, donwloaded())
    #asyncio.gather(*consumers,donwloaded())
        #await queues.join()
    #await asyncio.gather(donwloaded())
    


asyncio.run(main())
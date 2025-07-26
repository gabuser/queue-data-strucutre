import asyncio


queues = asyncio.Queue()
listas = []
with open('names.txt','r') as r:
    value = iter(r.read().split())
#value = (c for c in open('names.txt','r'))
#value.close()

print(type(value))

locks = asyncio.Lock()

async def producer(values):
    try:
        while True:        
            names = next(values)
            await queues.put(names)
    except StopIteration:
        pass

async def consumer():
    while True:
        async with locks:
            data = await queues.get()
            print(data)
        #print(queues.qsize())
            if(data is None):
            #print(data)
                    break
    print(queues.qsize())

async def main():
    count = 0
        
    for c in range(0,3):
        listas.append(producer(value))
        #count+=1   
    task_consumer = consumer()

    await asyncio.gather(*listas)
    await queues.put(None)
    await task_consumer
        
asyncio.run(main())
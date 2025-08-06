
import asyncio 
import aiofiles

tuples = iter((('file1.txt','hello world'),("file2.txt",'hello word2'),("file3.txt","hello world3")))
counter = 0
counter2 = 0

queue = asyncio.Queue()
queue2 = asyncio.Queue()

locks = asyncio.Lock()

async def getting():
    global counter

    while True:
        try:
            datas = next(tuples)
            await queue.put(datas)

        except StopIteration:
            break
    
    async with locks:
        counter+=1
    
    if(counter == 2):
        await queue.put(None)

async def consumer():
    while True:
        value = await queue.get()
        
        if(value is None):
            break
        else:
            await queue2.put(value)
            print(value)
    print(queue.qsize())

async def writing():
    global counter2

    while True:
        recived = await queue2.get()
        print(recived[0])
        async with aiofiles.open(recived[0], "a") as file:
            await file.write(recived[1])
        
        async with locks:
            counter2+=1 
        
        if(counter2 == 3):
            break
    
    print(queue.qsize())
    print(queue2.qsize())
async def main():
    prod =[]

    for _ in range(2):
        prod.append(getting())
    
    await asyncio.gather(*prod, consumer(), writing())

asyncio.run(main())
"""def chunking():

    for c in range(0, len(tuples),3):
        yield tuples[0:3][c:c +3]


for c in chunking():
    print(c)
   # print(c[counter+1])"""
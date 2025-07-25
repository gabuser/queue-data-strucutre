import asyncio 

numbers = (c for c in range(0,20))

queue = asyncio.Queue()
async def consumer():
    #global numbers
    num = [c for c in numbers]

    for c in num:
        await queue.put(c)


async def producer():
    for b in range(20):
        data = await queue.get()

        print(data)
    print(queue.qsize())
async def main():
    tasks = []

    async with asyncio.TaskGroup() as tg:

        for groups in range(4):
            #task = tg.create_task(consumer(numb))
            tasks.append(tg.create_task(consumer()))
            
        task2 = tg.create_task(producer())
    
        #await asyncio.gather(*tasks, task2)
asyncio.run(main())

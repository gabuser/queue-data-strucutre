import asyncio 


async def ola(times:int):

    await asyncio.sleep(times)
    return 'ola mundo'

async def main():

    task = asyncio.create_task(ola(2))
    task2= asyncio.create_task(ola(1))
    task3 = asyncio.create_task(ola(0.5))
    task4 = asyncio.create_task(ola(5))

    await task
    await task2 
    await task3 
    await task4 

    print(task,task2,task3, task4)

asyncio.run(main())
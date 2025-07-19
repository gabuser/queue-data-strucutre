import asyncio 
from sys import exit
requests = list()

line = asyncio.Queue()

async def note(requests:list,maxcapacity:int):
    for c in range(0,len(requests), maxcapacity):
        await asyncio.sleep(1)
        yield requests[c:c+maxcapacity]

async def organizing():
    async for start in note(requests, 2):
        for starts in start:
            await line.put(starts)

async def cooking():
    for c in range(len(requests)):
        await asyncio.sleep(2)
        done = await line.get()

        print(f'done:{done}')

def user():

    while True:
        value = input('insert your request or ctr+c to break it down:')

        if(value == 'q'):
            break

        else:
            requests.append(value)
        #await asyncio.gather(organizing(requests), cooking())

async def main():
    #user()
    if(requests):
        await asyncio.gather(organizing(), cooking())
    
user()
asyncio.run(main())
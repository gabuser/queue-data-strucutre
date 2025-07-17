import asyncio
queues = asyncio.Queue()
#q = queue.Queue()

listas = list(c for c in range(0,300))

def yieled():

    for c in listas:
        yield c

async def inputing():
    for b in yieled():
        await queues.put(b)

async def outputing():
    for lenght in range(queues.qsize()):
        data = await queues.get()
        print(data)

async def main():
    await asyncio.gather(inputing(),outputing())

asyncio.run(main())
"""def inputing():
    num = 0
    for c in listas:
        yield c 


for c in inputing():
    q.put(c)

for a in range(q.qsize()):
    print(q.get())"""
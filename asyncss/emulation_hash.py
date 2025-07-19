import asyncio 
from hashlib import sha256
from os import chdir, getcwd

queue = asyncio.Queue()
path = getcwd()
chdir(path)
lenghts = 0

names =(a for a in open("nomes.txt",'r'))

async def producer():
    global lenghts
    for a in names:
        lenghts+=1
        await queue.put(a.encode())

async def getting():
    for b in range(lenghts):
        yield await queue.get()

async def hashing():
    async for hashi in getting():
        await asyncio.sleep(1)
        print(f"\n {sha256(hashi).hexdigest()}")
        queue.task_done()

async def main():
    await asyncio.gather(producer(),hashing())

asyncio.run(main())
"""for a in names:
    q.put(''.join(a.splitlines()))

for a in range(q.qsize()):
    print(q.get())"""
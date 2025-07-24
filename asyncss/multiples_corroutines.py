import asyncio 
q = asyncio.Queue()
numbers = (c for c in range(0,10))
corroutines = []
consumers = []
#print(type(numbers))
async def producer():
    for numb in numbers:
        await q.put(numb)

async def consumer():
    for c in range(200):
        data = await q.get()
        
        await asyncio.sleep(1)
        print(data)
async def main():
    for a in range(0,11):
        corroutines.append(producer())
        #consumers.append(consumer())
    
    for b in range(3):
        consumers.append(consumer())
    
    await asyncio.gather(*corroutines,*consumers)

#for test in main():
asyncio.run(main())
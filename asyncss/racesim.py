import asyncio 
import random 

queues = asyncio.Queue()
corroutine = []
stop = True
runners= None
names = []

async def racers():
    global stop, runners
    while stop:
        await asyncio.sleep(1)
        runned = random.randint(0,5)
        await queues.put(runned)

        if(runned == 5):
            #queues.task_done()
            for c in range(1):
                await queues.put(None)
                #runners = names[c]
                #print(runners)
                #break
            stop = False

async def running():
    #global runners
    condition = True

    while condition:
        #distance = await queues.get()
        for b in range(6):
            distance = await queues.get()
            #await asyncio.sleep(1)
            runners = names[b]
            corroutines = corroutine[b]
            print(distance)
            #print(runners)
            
            if(distance is None):

                print(f"the runner {runners} won")
                print(corroutines)
                queues.task_done()
                condition = False
                #queues.task_done()

                #queues.task_done()
                #condition = False
    
    #print(f'the runner {runners} won')
async def main():

    for a in range(6):
        corroutine.append(racers())
        names.append(f"runner {a}")
    print(corroutine)
    d = asyncio.gather(*corroutine, running())
    await d

asyncio.run(main())
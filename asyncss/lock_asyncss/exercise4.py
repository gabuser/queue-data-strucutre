import asyncio 

queues = asyncio.Queue()
locks = asyncio.Lock()
#counter = 0

async def workers(ids):
    await asyncio.sleep(3)
    await queues.put(f'worker {ids} done')

    async with locks:
        #counter+=1
        print(f'worker {ids} is now working...')
    #print(f'worker: {counter}')

async def consumer():
    for _ in range(3):
        await asyncio.sleep(1)
        data = await queues.get()
        async with locks:
            if(data):
                #await asyncio.sleep(1)
                print(data)
        
            else:
                print("worker failed")
    print(queues.qsize())

async def main():
    #worker = list()

    async with asyncio.TaskGroup() as tg:
        worker = [tg.create_task(workers(_)) for _ in range(3)]
        consumers = tg.create_task(consumer())

asyncio.run(main())


"""import asyncio 

queues = asyncio.Queue()
locks = asyncio.Lock()
counter = 0

async def workers():
        global counter

        while (counter !=3):
    #for _ in range(3):
            await asyncio.sleep(3)
            await queues.put(f'worker {counter} done')

            async with locks:
                if(counter == 3):
                    #await queues.put(None)
                    break

                else:
                    print(f'worker: {counter}')
                    counter+=1

async def consumer():
    for _ in range(3):
        
        data = await queues.get()
        async with locks:
            if(data):
                print(data)
        
            else:
                print("worker failed")
    print(queues.qsize())

async def main():
    #worker = list()

    async with asyncio.TaskGroup() as tg:
        worker = [tg.create_task(workers()) for _ in range(3)]
        consumers = tg.create_task(consumer())

        esse codigo não funciona devido o global counter que está contido pelo lock

        imagina que existe uma sala, essa sala é possível que duas ou mais pessoas entrem, porém, o lock 
        protege essa sala com uma chave e cadeado, permitindo apenas que uma pessoa entre por vez, isso limita o uso do await queue, porque ele 
        não deixe que outras workers possam colocar os dados na fila.
        """

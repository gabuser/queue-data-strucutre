import asyncio 
import sys

queues = asyncio.Queue()

async def messaging():
    global user
    user = input("insert your name:")
    while True:
        #asyncio.thread cria ou separa qualquer função bloqueante python para uma outra thread separada.
        message = await asyncio.to_thread(input,"\n insert your message or ctr+c to quit:")
        if(message != 'q'):
            await queues.put(message)
        
        else:
            await queues.put(None)
            break

async def recive():
    while True:
        data = await queues.get()
        print(f'\n {user}: {data}')

        if(data is None):
            queues.task_done()
            break
async def main():
    await asyncio.gather(messaging(), recive())


asyncio.run(main())
    

        
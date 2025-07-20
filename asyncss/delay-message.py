import asyncio 
import random

queues = asyncio.Queue()

async def messaging():
    global user

    user = input('insert the user:')
    
    while True:
        message = await asyncio.to_thread(input,"\n insert the message you want to sending:")

        if(message == 'q'):
            await queues.put(None)
        
        else:
            await queues.put(message)

async def reciving():

    while True:

        recived = await queues.get()

        if(recived is None):
            break

        
        await asyncio.sleep(random.randint(0,10))
        print(f'\n {user}: {recived}')

async def main():
    await asyncio.gather(messaging(), reciving())

asyncio.run(main())


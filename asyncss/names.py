import asyncio 
queues = asyncio.Queue()

async def names():
    for c in range(0,11): #cria 10 tarefa hipotéticas
        await queues.put(f'task {c}') #o código coloca esses dados dentro de uma queue FIFO
        #await asyncio.sleep(1)

async def printing():
    while True: 
        data = await queues.get()#aqui ocorre a intercalação com o queue.put, uma hora ele coloca e outra hora tira.
        print(data)
        queues.task_done()# sinaliza que cada dado seja sinalizado como processado

        if data == 'task 10': #ao chegar na última tarefa, ele interrompe o loop.
            break

async def main():
    await asyncio.gather(names(),printing()) #cria as coroutines que vai fazer a intercalação real

asyncio.run(main())#roda as coroutines

    
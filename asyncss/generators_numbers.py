import asyncio 

queue = asyncio.Queue()
counter = 6 #contador fixo para tirar os elementos da fila(não recomendado para valores variados)

async def producer(): #função produtora, vai criar dados de entrada ou emular dados de entrada
    global counter
    for c in range(0,6):
        await asyncio.sleep(1) #simula o atraso dos dados
        yield c #função geradora, o que faz? ela retorna de forma eficientes os valores de um em um.

async def inputing(): #função de inputing é colocar os dados dentro da fila queue com a diferencia do yield
    async for b in producer():
        await queue.put(b)

async def consumer(): #função consumidora, vai consumir os dados, imprimindo eles na tela
    for a in range(counter):
        datareturned = await queue.get()
        #queue.task_done()

        print(datareturned)

async def main():
    await asyncio.gather(inputing(),consumer()) #agendando as coroutines para serem executadas


asyncio.run(main()) #executando todas as coroutines.
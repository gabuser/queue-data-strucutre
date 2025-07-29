import asyncio
import random 

queues = asyncio.Queue()
queues2 = asyncio.Queue()

locking = asyncio.Lock()
takss = 0
async def producer(ids:int):

    for _ in range(10):
        #await asyncio.sleep(1)
        #print(f"the worker {ids} is now working...")
        await queues.put(random.randint(0,200))
    
    #await queues.put(None)
async def calculate():
    #global counter

    while(True):
    #for __ in range(30):
        data= await queues.get() #supondo que tenha 3 itens aqui

        if(data is None):
            #for _ in range(3):
            await queues2.put(None)

            break

        #async with locking:
        await asyncio.sleep(1)
        calculation = data**2
                #counter+=1
        
        await queues2.put(calculation)

async def showing():
    #for sentinel in range(30):
    global takss
    while True:
        processed = await queues2.get()
        print(processed)

        async with locking:
            takss+=1
        
        print(f'\n tasks executed: {takss}')
        if(processed is None):
            break

    print(queues.qsize())


async def main():
    producers = []
    calculaters = []
    #condition = 0

    for _ in range(3):
        producers.append(producer(_))
        #condition+=1
    
    for _ in range(2):
        calculaters.append(calculate())

    #queues.put(None)
    await asyncio.gather(*producers)

    for a in range(2):
        await queues.put(None)

    await asyncio.gather(*calculaters,showing())
    #await queues.join()
    #await queues.put(None)
    #queues.put(None)
    #condition+=1
asyncio.run(main())

"""
pipeline simples. 

o que acontece nesse código: estamos criando duas filas, a primeira fila é usada para passar e enfilerar os números dentro da queue, a função produtora 
irá intercalar entre as corroutines para escolher um número aleatório e passar para a fila. A segunda fila é usada para armazenar a potência do quadrado desse número escolhido,
então o produtor escolhe o número, coloca na fila e enfileira e a função consumidora pega esse valor e calcula a sua potência quadrada desse número e passa para a fila 2, fila
reservada para números calculados, a função consumidora está usando duas corroutines para auxiliar nesse processo.

quando a função produtora parar de produzir os números, a função main irá sinalizar uma sentinela para que a função consumidora e shwoing não fique esperando eternamente por dados da fila, sinalizando a hora 
de parar. nesse meio tempo, a função showing mostra o resultado da tela que são passados pela função consumidora até não houver mais dados e todas serem consumidas da fila por completo.


"""
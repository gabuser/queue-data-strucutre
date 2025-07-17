import asyncio
tasks = [] #lista para agendar as coroutines

async def counting(): #função que vai contar 1 e 2
    print('one')
    #await asyncio.sleep(1) #simula o tempo de intercalação entre as courotines
    print('two')

async def main(): #função que vai criar as coroutines
    for c in range(0,20): #cria 19 coroutines ao invés de await asyncio.gather(counting(),counting()...)
        tasks.append(counting())
    
    await asyncio.gather(*tasks) #cria as couroutines e deixa elas em prontidão

asyncio.run(main()) #executa as mesmas. 
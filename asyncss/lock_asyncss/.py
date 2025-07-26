import asyncio

queues = asyncio.Queue()

with open('names.txt', 'r') as r:
    value = iter(r.read().split())

num_producers = 3
SENTINEL = None

# ---

async def producer(values):
    try:
        while True:
            name = next(values)
            # await queues.put(name)  # Esta linha foi removida para evitar duplicação no print
            await queues.put(name)
    except StopIteration:
        pass

async def consumer():
    while True:
        data = await queues.get()
        print(queues.qsize())
        if data is SENTINEL:
            break
        print(f"Consumidor pegou: {data}")
        queues.task_done()

# ---

async def main():
    producer_tasks = [asyncio.create_task(producer(value)) for _ in range(num_producers)]
    consumer_task = asyncio.create_task(consumer())
    
    # Espera que todos os produtores terminem.
    await asyncio.gather(*producer_tasks)
    
    print("\nTodos os produtores terminaram de colocar os itens na fila.")
    
    # Agora que sabemos que os produtores acabaram, enviamos o sinal de término.
    await queues.put(SENTINEL)
    
    # Esperamos que o consumidor termine.
    await consumer_task
    
    await queues.join()
    print("Todas as tarefas foram concluídas.")

asyncio.run(main())
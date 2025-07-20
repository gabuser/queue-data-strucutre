import asyncio

data = []
queues = asyncio.Queue()

async def producer(emails:list, workers:int):
    for c in range(0, len(emails), workers):
        
        await asyncio.sleep(1)
        yield emails[c:c+workers]

async def consumer():
    async for c in producer(data, 3):
        for b in c:
            await queues.put(b)

async def sending():

    for c in range(len(data)):
        value = await queues.get()

        #await asyncio.sleep(1)

        print(f'sending email to: {value}')

async def main():
    await asyncio.gather(consumer(), sending())

while True:
    try:
        datas = input("insert the emails u want to send:")

        if datas =='q':
            break

        else:
            data.append(datas)
    
    except KeyboardInterrupt:
        break

asyncio.run(main())

"""nem toda função assíncrona é uma função assíncrona, para que ela seja assíncrona, a função 
precisa ter um await que será gerenciado pelo event loop. sem o await, a função se torna uma corroutine
síncrona. podemos usar await para qualquer tarefa ou coroutine que precisa esperar ou ser gerenciado pelo
event loop. 

a primeira função chamada de "producer" na verdade uma função assíncrona geradora, isso quer dizer que ele 
é um objeto gerador que teem como principal função distribuir os dados em chunks menores para serem 
consumidos pela fila queue.

o await pausa e gerencia as tarefas que vão entrar no event loop e as tarefas que estarão em espera
enquanto o event loop faz ou executa uma determinada tarefa. 

é como se ele fosse um organizador de entrada de uma festa de balada, se a balada estiver muito cheia, 
o segurança vai pedir para o fluxo inteiro parar e esperar até alguem sair para que possa liberar a proxima 
pessoa a entrar. o mesmo ocorre aqui."""


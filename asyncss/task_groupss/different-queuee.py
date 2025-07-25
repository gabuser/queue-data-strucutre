import asyncio 
import random

queues = asyncio.Queue()
#counter = 0

async def producer():    
    for b in range(0,5):
        await queues.put(random.randint(0,100))

async def consumer():
    for c in range(15):
        data = await queues.get()
        print(data)

async def main():

    async with asyncio.TaskGroup() as tg:

        corroutines = [tg.create_task(producer()) for _ in range(3)] 
        
        consumers = tg.create_task(consumer())

asyncio.run(main())

"""
    estamos criando 3 corroutines, como cada corroutine é um objeto, ela tem suas propriedades como iteração, fila ou queue e também tem a sua propria
    geração de números aleatórios. Quando criamos uma lista de corroutines, estamos definindo que cada uma tem suas proprias propriedades espécificas. 
    cada uma vai gerar um número aleatório e colocar na sua própria fila, isso pode consumir muita memoria senão usar com cuidado, podendo em muitos momentos
    gerar memory error ou erros de buffer. apesar de ser python, não está blindado a esses erros. 

    a lógica do consumer é simples, é apenas um consumidor que vai pegar os resultados da fila e imprimir na tela ou retornar os dados processados. 

    por debaixo dos panos isso está ocorrendo: 3 corroutines x 5 números gerados, totalizando 15 elementos na fila. 5+5+5 cada uma sendo uma fila. 
    e para o consumer ele faz: -5, -5, -5 até esvaziar a fila por completo.
"""
import threading
import queue
import time

semaforo = threading.Semaphore(2)
queues = queue.Queue()

def dados(dado:int) -> str:
    for c in dado:
        queues.put(c)

def exibir():
    with semaforo:
            time.sleep(1)
            print(queues.get())

threads = list()

for _ in range(1):
    th1 = threading.Thread(target=dados, args=([1,2,3,4,5],))
    th1.start()
    threads.append(th1)

for _ in range(5):
    th2 = threading.Thread(target=exibir)
    th2.start()
    threads.append(th2)


for thread in threads:
    thread.join()

"""
estamos usando o modelo de controle de semafaros aqui. o que ele faz? um controle de semafáro 
controla a quantidade de threads que pode consumir um recurso computacional por vez. Diferentimente do 
sistema de threads como conhecemos, as threads podem consumir todas de uma vez com a sincronização correta 
para evitar concorrência de recursos e também overwriting, o que está ocorrendo nesse código é que estou 
definindo a quantidade de threads que pode consumir por vez um recurso, nesse caso acessar a função consumidora
que vai retornar ou exibir os dados processados na tela. eu criei uma lista de 5 elementos númericos que será enviado
para uma queue FIFO, essa queue vai enfilerar os dados e mandar para a threads consumidoras e cada uma por vez irá 
enviar ou exibir os dados na tela, como o queue é thread safe, então há risco de concorrência aqui.


"""
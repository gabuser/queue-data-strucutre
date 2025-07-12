import threading
import time 
import queue 
q= queue.Queue(5)
lines = list()
datas :str

def production():
    for c in range(20):

        time.sleep(1)
        if(q.full()): #verifica se o buffer está cheio e emite uma mensagem de erro
            print("o buffer está cheio")
            #time.sleep(1)
            #datas = q.get()
        
        q.put('dados'+str(c))# 5 dados inicialmente(limite que foi estabelicido no buffer ali em cima)

def consumer(): #função consumidora, ela vai transportar os dados para processamento 

    while True: 
        time.sleep(5)#simula o tempo de espera, os dados saem na ordem de entrada usando FIFO
        print("buffer foi liberado para uso!")

        datas = q.get()#libera os dados da fila, até não houver mais nenhum dado a ser liberado
        print(datas)
        if(datas is None): #verifica se há dados para serem transferidos
          q.task_done() #emite um sinal de de finalização 
          break

#production()
th1 = threading.Thread(target=production) #definindos as threads
th2 = threading.Thread(target=consumer)
#consumer()
th1.start()
th2.start()


#q.put(None)
#consumer()

th1.join()
q.put(None) #sinalizando manulalmente para que as thread finalize a tarefa.
#consumer()
th2.join()

#isfinished()
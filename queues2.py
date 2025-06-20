import queue 
import threading 
import time 


q = queue.Queue(10)#buffer não foi especificado, isso pode causar muitos erros de memoria no futuro

def line():
    for c in range(20):
        q.put("dados"+str(c)) #inserindo valores dentro da fila FIFO
    

def printingout():
    for c in range(20):
        time.sleep(1)
        print(q.get())

th = threading.Thread(target=line)
#th2 = threading.Thread(target=printingout)
th2 = threading.Thread(target=printingout)
th.start()
#th2.start()
th2.start()

th.join()
th2.join()
#th2.join()

"""
    duas threads são criadas para gerenciar o fluxo de entrada e saída dos dados
    a primeira thread coloca os supostos dados na memoria ou na fila queue, enquanto ao 
    mesmo tempo a segunda thread transfere esses dados para serem mostrados na tela. 
    o exemplo usado é um FIFO que é gerenciado pela lib queue. 

    como as duas threads acessam a fila simultaneamente como uma lista, a queue consegue 
    gerenciar qual dados foram acessadas na sequência e qual ainda não foi.
"""
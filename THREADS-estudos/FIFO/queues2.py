import queue 
import threading 
import time 


q = queue.Queue()#buffer não foi especificado, isso pode causar muitos erros de memoria no futuro

def line(): #produtor, ele vai gerar os dados e colocar dentro da fila para serem transferidos da memoria
    for c in range(20):
        q.put("dados"+str(c)) #inserindo valores dentro da fila FIFO
    #q.task_done()
    #q.task_done()

def printingout(): # consumidor, ele vai consumir os dados e fazer o processamentos dos dados
    #for c in range(20):
    while True:
        #time.sleep(1)
        datas = q.get()
        print(datas)

        if(datas is ""):
            q.task_done()
            break


    #q.join()


th = threading.Thread(target=line)
#th2 = threading.Thread(target=printingout)
th2 = threading.Thread(target=printingout, daemon=True)
th3 = threading.Thread(target=printingout,daemon=True)
th.start()
#th2.start()
th2.start()
th3.start()

#th.join()
q.put("")
q.put("")
th2.join()
th3.join()

#q.put(None)
#th2.join()

"""
    duas threads são criadas para gerenciar o fluxo de entrada e saída dos dados
    a primeira thread coloca os supostos dados na memoria ou na fila queue, enquanto ao 
    mesmo tempo a segunda thread transfere esses dados para serem mostrados na tela. 
    o exemplo usado é um FIFO que é gerenciado pela lib queue. 

    como as duas threads acessam a fila simultaneamente como uma lista, a queue consegue 
    gerenciar qual dados foram acessadas na sequência e qual ainda não foi.
"""
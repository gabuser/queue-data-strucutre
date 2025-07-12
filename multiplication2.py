import threading
import queue

locking = threading.Lock()
semaphore = threading.Semaphore(4)
queues = queue.Queue()
generated = [c for c in range(0,200)]

def workers(numbers:list ):
    for get in numbers:
        queues.put(get)

def consumer(multiplacatedfor:int):
     while(True):
        with semaphore:
            number = queues.get()
            with locking:
                if(number is not None):
                    calculus = (multiplacatedfor*number)
                    print(f'result:{calculus}')
                
                else:
                    break
threads = list()
def main():
    for _ in range(1):
        worker = threading.Thread(target=workers, args=(generated,))
        worker.start()
        worker.join()
        #threads.append(worker)
    
    for _ in range(21):
        queues.put(None)
        
    for _ in range(21):
        consumers = threading.Thread(target=consumer, args=(2,))
        threads.append(consumers)
    
    for counter in range(0,len(threads),2):
        chunk = threads[counter:counter +2]

        for t in chunk: #inicie duas threads por vez
            t.start()
        
        for t in chunk: #após finalizar as duas threads, passe para o próximo par ou dupla de threads.
             t.join()

        yield chunk #yield que retorna aos poucos 
    
for c in main():
    print(c)

"""

        o que está acontecendo? 
        foi implementado o chunk com objetivo de controlar a forma como as threads estão
        sendo distribuídas para acessar um determinado recurso. sem as chunks, o próprio 
        sempahore vai limitar o uso das threads para 4 threads por vez, entretanto ao fazer isso
        ele vai simplesmente jogar as 4 threads de uma única vez só para executar as tarefas, em 
        casos mais complexos, isso pode sobrecarregar o CPU com muitas threads sendo executada uma única vez
        ao limitar, estamos falando para as threads iniciarem em grupos de pares cada, evitando sobrecarregamentos
        da CPU
"""
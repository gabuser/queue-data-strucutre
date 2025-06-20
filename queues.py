
from collections import deque

class Queue:

    def __init__(self):
        self.elements =deque()
    
    def enqueue(self,element:str):
        self.elements.append(element) #função para os dados dentro da queue
    
    def dequeue(self): #retira os elementos da fila na ordem de chegada, o primeiro a sair foi o primeiro a entrar
        return self.elements.popleft()
    
fifo = Queue() #FIFO object para agir como uma FIFO 

for c in range(5): #simula 5 dados entrando
    value = "dados"+str(c)
    fifo.enqueue(value)

for removing in range(5): #simula a sua saída
    print(fifo.dequeue())
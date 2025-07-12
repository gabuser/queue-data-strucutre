import queue
lists = [1,2,3,4,5,6]
q = queue.Queue()

for line in lists:
    q.put(line)#colocando todos os dados dentro de uma fila ou sequência de execução para não correr concocorrência
#print(q.get())
for _ in range(len(lists)):
  print(q.get())
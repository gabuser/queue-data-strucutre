
import os 
import time

path = os.getcwd()
files = os.listdir(path)
#tuples = ((files[2], open(files[2],"r").read()), (files[3], open(files[3],"r").read()))
#tuples = (files[2],(open(files[2],"r").read()))
counter = 0 
counter2 = 0
tuples =list()
#while True:
#print(files)
for c in range(len(files)):
    data = open(files[c],'r').read()

    filename = files[c]
    #print(data)
    if(not filename.endswith(".py")):
        tuples.append((filename,data))
    
print(tuples[0][1][0])
def chunking():
    global counter, counter2

    #for _ in range(len(tuples)):
    #while True:
    while True:
        try:
            values = tuples[counter][1][counter2]
            counter2+=1 
            #time.sleep(1)
            print(end=values)
            #time.sleep(1)
            #print(counter2)
            #print(counter2)
        except IndexError:
            counter2+=0
            counter+=1
            #print(counter2)
            #pas
        
        if(counter == len(tuples)):
            break
chunking()
""""def chunks():
        global counter
        while True:
            try:
                for c in range(0,len(tuples),20):
                    yield tuples[counter][1][c:c+20]
            
                counter+=1 

            except IndexError:
                 counter= 0 
            
            if(counter > len(tuples)):
                 break"""


"""se caso o usuário quiser colocar todos os arquivos, então  ele vai
incrementar uma range e iterar sobre eles

for lenght in range(len(os.lisdir())

cada file[range_lenght] ele vai enfilerando e colocando indices e seus dados representantes dentro de uma tupla normalmente
se caso ele decidir escolher o arquivo, fica mais fácil, so fazer uma busca binária para pegar o arquivo e colocar
dentro da tupla enfilerada que vai ser produzida na queue)"""
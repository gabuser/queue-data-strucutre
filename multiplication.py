import threading
import time 
import queue

queues = queue.Queue()
locking = threading.Lock()
sempahore = threading.Semaphore(2)

def worker(numbers:list,multiplicatedfor:int):
    for number in numbers:
        with locking:
            result = (number *multiplicatedfor)

        queues.put(result)

def consumer(thread_id:list):
    showing = queues.get()
    if(not queues.empty()):
        with locking:
            time.sleep(1)
            print(f'\n result of the multiplication of the thrad{thread_id}:{showing}')

thread = list()

for ids in range(21):
    workers = threading.Thread(target=worker, args=([c for c in range(21)],2,))
    consumers = threading.Thread(target=consumer,args=(ids,))
    workers.start()
    consumers.start()

    thread.append(workers)
    thread.append(consumers)

for threads in thread:
    threads.join()

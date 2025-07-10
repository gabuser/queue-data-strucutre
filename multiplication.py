import threading
import queue

queues = queue.Queue()
locking = threading.Lock()
sempahore = threading.Semaphore(1)

def worker(numbers:list,multiplicatedfor:int):
    for number in numbers:
        with locking:
            result = (number *multiplicatedfor)

        queues.put(result)

def consumer(thread_id:list):
    showing = queues.get()
    if(not queues.empty()):
        with locking:
            print(f'\n result of the multiplication of the thrad{thread_id}:{showing}')

thread = list()

for _ in range(1):
    workers = threading.Thread(target=worker, args=([c for c in range(21)],2,))
    workers.start()
    thread.append(workers)

for ids in range(21):
    consumers = threading.Thread(target=consumer,args=(ids,))
    consumers.start()
    thread.append(consumers)

for threads in thread:
    threads.join()

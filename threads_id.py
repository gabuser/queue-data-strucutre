import threading
import queue
import time 
queues = queue.Queue()
semaphore = threading.Semaphore(3)
locking = threading.Lock()

def producer_queue(id:list):
    for c in id:
        queues.put(c)

def priting():
    #global ids

    with semaphore:
        ids = queues.get()

        print(f'\n thread {ids} is now running...')
        time.sleep(1)
    
    with locking:
        print(f"\n thread:{ids} is now finished")

thread = list()

for _ in range(1):
    prouducerthread = threading.Thread(target=producer_queue, args=([c for c in range(11)],))
    prouducerthread.start()
    thread.append(prouducerthread)

for _ in range(11):
    consumerthread = threading.Thread(target=priting)
    consumerthread.start()
    #loginthread.start()

    thread.append(consumerthread)
    #thread.append(loginthread)

for thr in thread:
    thr.join()

    
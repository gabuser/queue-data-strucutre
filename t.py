import threading
import queue
import time

locking = threading.Lock()
semaphore = threading.Semaphore(2)
queues = queue.Queue()
generated = [c for c in range(0, 200)]

def workers(numbers: list):
    for get in numbers:
        queues.put(get)

def consumer(multiplied_for: int):
    with semaphore:
        if not queues.empty():
            number = queues.get()
            with locking:
                calculus = multiplied_for * number
                print(f'result: {calculus}')
            queues.task_done()

worker_thread = threading.Thread(target=workers, args=(generated,))
worker_thread.start()

# Aguarda o worker colocar itens na fila (simples delay)
time.sleep(0.1)

consumer_threads = []
for _ in range(8):  # por exemplo, 8 consumers
    t = threading.Thread(target=consumer, args=(2,))
    consumer_threads.append(t)

def main():
    for i in range(0, len(consumer_threads), 2):  # chunk de 2
        chunk = consumer_threads[i:i+2]

        for t in chunk:
            t.start()

        for t in chunk:
            t.join()

        yield chunk

for c in main():
    print(f"Chunk finalizado: {c}")

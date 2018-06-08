import threading
import random
import time
import queue
from threading import BoundedSemaphore


class Violinist(threading.Thread):
    def __init__(self, semaphore, queue_violin, queue_bow, mutex_violin, mutex_bow, name):
        threading.Thread.__init__(self)
        self.semaphore = semaphore
        self.queue_violin = queue_violin
        self.queue_bow = queue_bow
        self.mutex_violin = mutex_violin
        self.mutex_bow = mutex_bow
        self.name = name

    def run(self):
        i = 0
        while i < 6:
            self.semaphore.acquire()
            viol, bow = self.get_instrument()
            time.sleep(random.randint(1, 5))
            self.put_instrument(viol, bow)
            self.semaphore.release()
            time.sleep(2)
            i += 1

    def get_instrument(self):
        viol = self.get_instrument4thread(mutex_violin, queue_violin)
        bow = self.get_instrument4thread(mutex_bow, queue_bow)
        return viol, bow

    def put_instrument(self, viol, bow):
        self.put_instrument4thread(mutex_violin, queue_violin, viol)
        self.put_instrument4thread(mutex_bow, queue_bow, bow)

    def get_instrument4thread(self, mutex, queue):
        mutex.acquire()
        while (queue.qsize() == 0):
            mutex.wait()
        part_instrument = queue.get()
        print(self.name + ' take ' + part_instrument)
        mutex.notify_all()
        mutex.release()
        return part_instrument

    def put_instrument4thread(self, mutex, queue, part_instrument):
        mutex.acquire()
        queue.put(part_instrument)
        print(self.name + ' put ' + part_instrument)
        mutex.notify_all()
        mutex.release()


maxconnections = 3
pool_sema = BoundedSemaphore(value=maxconnections)

mutex_violin = threading.Condition()
queue_violin = queue.Queue(3)
mutex_bow = threading.Condition()
queue_bow = queue.Queue(3)

for item in range(1, 4):
    queue_violin.put('violin' + str(item))
    queue_bow.put('bow' + str(item))

for item in range(1, 7):
    violinist = Violinist(pool_sema, queue_violin, queue_bow, mutex_violin, mutex_bow, ('Violinist' + str(item)))
    violinist.start()
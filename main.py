<<<<<<< HEAD
from queue import Queue

from threading import Thread

import time

import random

# Crear cola

q = Queue(10)

def producer(name):
   """Productor"""
   count = 1 
   while True:
      if not q.full():
        item = random.randint(1, 10)
        q.put(item)
  
        print(f"{name} está produciendo el bollo {count}")
        
        count+=1

        time_to_sleep = random.randint(1, 10)
        time.sleep(time_to_sleep)

def customer(name):

  """consumidor"""
  count = 1
  while True:
        if not q.empty():
          
          q.task_done()
          print(f"El consumidor- {name} está comiendo el bollo {count}")
          count+=1
          time_to_sleep = random.randint(1, 10)
          time.sleep(time_to_sleep)


if __name__ == '__main__':

    t1 = Thread(target=producer,args=("Maestro Rubén",))

    t2 = Thread(target=customer,args=("Los alumnos",))

    t1.start()

    t2.start()


=======
import threading
import time
import logging
import random
import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 10
q = Queue.Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1,10)
                q.put(item)
                logging.debug('Putting ' + str(item)
                            + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                logging.debug('Getting ' + str(item)
                            + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return

if __name__ == '__main__':

    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)
>>>>>>> origin/main

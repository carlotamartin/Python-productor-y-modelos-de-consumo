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



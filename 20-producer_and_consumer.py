import time
import queue
import random
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')

"""
Problema productor-consumidor

El programa describe dos procesos, productor y consumidor,
ambos comparten un buffer de tamaño finito.
La tarea del productor es generar un producto, almacenarlo y comenzar nuevamente;
mientras que el consumidor toma (simultáneamente) productos uno a uno.

El Problema consiste en que el productor no añada más productos que la capacidad del buffer 
y que el consumidor no intente tomar un producto si el buffer está vacío.
"""

# Indicamos el tamaño máximo que puede almacenar la cola
queue = queue.Queue(maxsize=10)

# Definimos el productor
# Va a generar un elemento aleatorio y lo va a almacenar en la cola siempre que no esté llena
def producer():
	while True:
		if not queue.full():
			item = random.randint(1, 10)
			queue.put(item)

			logging.info(f'Nuevo elemento dentro de la cola {item}')

			time_to_sleep = random.randint(1, 3)
			time.sleep(time_to_sleep)


# Mientras la cola no esté vacía el consumidor estará obteniendo elementos
def consumer():
	while True:
		if not queue.empty():
			item = queue.get()

			queue.task_done()

			logging.info(f'Nuevo elemento obtenido {item}')

			time_to_sleep = random.randint(1, 3)
			time.sleep(time_to_sleep)



if __name__ == '__main__':
	
	thread_producer = threading.Thread(target=producer)
	thread_consumer = threading.Thread(target=consumer)

	thread_producer.start()
	thread_consumer.start()
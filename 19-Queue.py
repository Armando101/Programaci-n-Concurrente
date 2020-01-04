import time
import logging
import threading
import queue

"""
Vamos a utilizar el módulo queue
Queue es una estructura de datos de tipo FIFO
"""

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def show_elements():
	# El método empty perimite conocer si la cola está vacía
	while not queue.empty():
		item = queue.get()

		logging.info(f'El elemento es: {item}')

		# task_done indica que el thread está liberando la cola para que otro thread pueda usarla
		queue.task_done()

		time.sleep(0.5)

if __name__ == '__main__':
	queue = queue.Queue()

	for val in range(1, 20):
		queue.put(val)

	logging.info('La cola ya posee elementos')

	for _ in range(4):
		thread = threading.Thread(target=show_elements)
		thread.start()
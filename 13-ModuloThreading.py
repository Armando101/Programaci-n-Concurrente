import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Con el módulo threading podemos obtener distintos datos del thread actual

def nueva_tarea():
	current_thread = threading.current_thread()
	
	# Obtener nombre del thread
	name = current_thread.getName()

	# Obtener el id del thread
	id = threading.get_ident()

	logging.info(f'El Thread actual es: {current_thread} y su nombre es {name}')
	logging.info(f'El id actual es {id}')


if __name__ == '__main__':
	# Es posible colocarle un nombre al thread

	thread1 = threading.Thread(target=nueva_tarea, name = 'thread-PROTECO')
	thread1.start()

	# Podemos ver los threads que están vivos en nuestro código
#	logging.info(f'Los threads vivos son: {threading.enumerate()}')
	
	# También es posible hacerlo de la siguiente manera
	for thread in threading.enumerate():
		logging.info(thread)
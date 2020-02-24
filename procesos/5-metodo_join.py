import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(process)s %(processName)s %(message)s')

def nuevo_proceso(mensaje):
	logging.info('Hola, soy un nuevo proceso')

	time.sleep(5)

	logging.info(mensaje)
	logging.info('Fin del proceso')

if __name__ == '__main__':

	process = multiprocessing.Process(target=nuevo_proceso, name='proceso-hijo', daemon=True, args=('Mensaje desde un argumento',))
	process.start()

	# Detiene momentaneamente el proceso padre hasta que el proceso hijo termine su ejecución
	process.join()

	logging.info('Hola, desde el proceso padre')
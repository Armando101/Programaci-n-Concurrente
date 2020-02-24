import os
import time
import logging
import multiprocessing

# El proceso padre siempre tendrá un id menor que el del hijo

logging.basicConfig(level=logging.DEBUG, format='%(process)s %(processName)s %(message)s')

def nuevo_proceso(mensaje):
	logging.info('Hola, soy un nuevo proceso')

	time.sleep(5)

	logging.info(mensaje)
	logging.info('Fin del proceso')

if __name__ == '__main__':
	# Los arguementos se pueden pasar con tuplas o diccionarios
	# Tuplas: args=('Mensaje desde un arguemento',)
	# Diccionarios: kwargs= {'mensaje':Nuevo mensaje desde un arguemento}
	process = multiprocessing.Process(target=nuevo_proceso, name='proceso-hijo', args=('Mensaje desde un argumento',))
	process.start()

	logging.info('Hola, desde el proceso padre')
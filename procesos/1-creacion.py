import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def nuevo_proceso():
	logging.info("Hola, soy un nuevo proceso")

	time.sleep(30)

	logging.info("Fin del proceso")


if __name__ == '__main__':
	# El proceso de creación de procesos es igual al de los threads
	proceso = multiprocessing.Process(target = nuevo_proceso)

	proceso.start()

	logging.info("Hola desde el proceso padre")
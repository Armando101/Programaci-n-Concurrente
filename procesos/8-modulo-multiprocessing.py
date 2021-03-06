import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

if __name__ == '__main__':

	# Podemos obtener infomación de los procesos a partir del
	# Módulo multiprocessing
	
	current_process = multiprocessing.current_process()

	pid = current_process.pid
	name = current_process.name

	logging.info(f'El proceso actual es: {current_process}')
	logging.info(f'El id del proceso actual es: {pid}')
	logging.info(f'El nombre del proceso actual es: {name}')
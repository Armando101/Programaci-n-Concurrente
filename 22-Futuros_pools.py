import time
import requests
import threading
import logging
from concurrent.futures import ThreadPoolExecutor

"""
El método sumbit me regresa un futuro
Esto significa que podemos programar acciones que queremos se ejecuten posteriormente
"""
logging.basicConfig(level = logging.DEBUG, format='%(threadName)s : %(message)s')

URLS = [
	'https://proteco.mx',
	'https://twitter.com/home',
	'https://es.stackoverflow.com',
	'https://about.gitlab.com',
	'https://github.com',
	'https://www.youtube.com'
]


def generate_request(url):
	return requests.get(url), url

def check_status_code(future):
	response = future.result()
	logging.info(f'La respuesta del servidor {response[1]} es: {response[0].status_code}')

def math_operation(n1, n2):
	return n1 + n2

if __name__ == '__main__':
	# Generamos la piscina de threads

	with ThreadPoolExecutor(max_workers=2) as executor:
		for url in URLS:
			# Asignamos el futuro a una variable
			future = executor.submit(generate_request, url)

			# Agregamos un callback al futuro
			future.add_done_callback(check_status_code)

			# Los threads dentro de la piscina los podemos utilizar N cantidad de veces con N cantidad de tareas
			# Probemos ejecutando una nueva tarea
			future = executor.submit(math_operation, 10, 20)
			future.add_done_callback(
					lambda future: logging.info(f'El resultado de la operación es : {future.result()}')
				)
			
"""
		# Otra manera de hacer lo anterior
		futuros = [ executor.submit(generate_request, url) for url in URLS ]

		for futuro in futuros:
			futuro.add_done_callback(
					lambda future: check_status_code(future.result())
				)
"""
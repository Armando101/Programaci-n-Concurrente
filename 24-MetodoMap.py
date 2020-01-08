"""
El método map funciona igual que la función map
La diferencia es que el método ejecuta la función de manera concurrente y no secuencial
"""

import time
import requests
import threading
import logging

from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor



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

def check_status_code(response, url):
	logging.info(f'La respuesta del servidor {url} es: {response.status_code}')

def math_operation(n1, n2):
	return n1 + n2

if __name__ == '__main__':
	
	with ThreadPoolExecutor(max_workers=2) as executor:
		futuros = [executor.submit(generate_request, url) for url in URLS]

		# La función as_completed recibe una lista de futuros y retorna los futuros que posean un valor, es decir, los que ya han sido completados
		for futuro in as_completed(futuros):
			response, url = futuro.result()

			check_status_code(response, url)
			

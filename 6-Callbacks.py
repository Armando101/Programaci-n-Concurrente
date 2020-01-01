import logging
import requests
import threading

# Los callbacks son útiles para definir acciones que van a ser ejecutadas en un futuro

logging.basicConfig(level = logging.DEBUG, format = '%(message)s')

def get_pokemon_name(response_json):
	name = response_json.get('forms')[0].get('name')
	logging.info(f'El nombre del pokemon es : {name}')

def get_name_random(response_json):
	name = response_json.get('results')[0].get('name').get('first')
	logging.info(f'El nombre del usuario es : {name}')

def error():
	logging.error('No es posible completar la operación')

# Esta función hace una petición y ejecuta un callback dependiendo si la petición fue exitosa
def generate_request(url, success_callback, error_callback):
	response = requests.get(url)

	# Si la petición fue exitosa ejecutamos un callback
	# Estos callback's no se ejecutan directamente sino que esperan a la respuesta del servidor
	if response.status_code == 200:
		success_callback(response.json())
	else:
		error_callback()


if __name__ == '__main__':
	thread1 = threading.Thread(target=generate_request, kwargs={
								'url' : 'https://pokeapi.co/api/v2/pokemon/1',
								'success_callback' : get_pokemon_name,
								'error_callback' : error
								})

	thread2 = threading.Thread(target=generate_request, kwargs={
								'url' : 'https://randomuser.me/api',
								'success_callback' : get_name_random,
								'error_callback' : error
								})

	thread1.start()
	thread2.start()
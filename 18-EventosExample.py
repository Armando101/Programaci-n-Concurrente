import time
import logging
import threading
import requests


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

# Definimos dicionario vacío
user = dict()

def generate_request(url, event):
	global user

	response = requests.get(url)

	if response.status_code == 200:
		response_json = response.json()

		user = response_json.get('results')[0]

		# Damos la señal para que reaude los procesos
		event.set()

def show_user_name(event):
	logging.info('Función show_user_name')

	# Aquí marca un error debido a que intenta obtener información de un dato NoneType
	# Esto porque la función se ejecuta antes de que user tenga un valor
	# Esto por el tiempo que toma hacer la petición
	# Esta función se ejecuta antes de que la petición se realice
	# Esto se soluciona con eventos

	# Esperamos hasta que la señal sea dada
	event.wait()

	name = user.get('name').get('first')

	logging.info(f'El nombre del usuario es: {name}')


if __name__ == '__main__':

	event = threading.Event()

	thread1 = threading.Thread(target=generate_request, args=('http://randomuser.me/api', event))
	thread2 = threading.Thread(target=show_user_name, args=(event,))

	thread1.start()
	thread2.start()
import time
import logging
import threading
import requests

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Un demonio es un proceso que se ejecuta en background
# El demonio finaliza cuando el main thread finalice

def thread():
	logging.info('Hola, soy un thread normal')
	time.sleep(2)
	logging.info('El programa finaliza caundo YO finalizo')

# La siguiente función será un demonio que se ejecutará en background
# Finalizará hasta que el main thread finalice
def daemon_thread():
	while True:
		logging.info('Nos ejecutamos en segundo plano, en background')
		time.sleep(0.5)

if __name__ == '__main__':
	# Para indicar que una función será un demonio se hace de la sguiente manera
	# Indicamos el parámetro daemon como True
	thread = threading.Thread(target=daemon_thread, daemon=True)
	thread.start()

	input('Presiona una tecla para finalizar el thread principal')
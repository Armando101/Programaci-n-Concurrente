import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

# Se pueden ejecutar tareas mediante funciones pero también es posible con clases
# Podemos generar nuestras propias clases para que se conviertan en threads
# Para esto la clase debe heredar de la clase Thread

class ThreadProteco(threading.Thread):
	def __init__(self, name, daemon=False):
		threading.Thread.__init__(self, name=name, daemon=daemon)

	# Sobreescribimos el método run
	# En este método van las tareas que queremos se ejecuten de forma concurrente
	def run(self):
		while True:
			logging.info('Aquí debemos colocar todas las tareas que queremos se ejecute de forma concurrente')
			time.sleep(1)


if __name__ == '__main__':
	# El método start internamente hará el llamado al método run
	thread = ThreadProteco('Thread-PROTECO', True)
	thread.start()


	time.sleep(3)
	logging.info('FIN del programa')
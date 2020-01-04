import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')

"""
Un evento internamente contiene una bandera, verdadero o falso
Por default la bandera comienza en falso
Una vez la bandera cambia a verdadero se dispara una señal
Todos los threads que se encuentren a la espera de esa señal van a reanudar su ejecución
Podemos conocer si la señal fue dada através del método is_set()

Podemos establecer la bandera neuvamente en false con el método clear
"""

def thread_1(event):
	logging.info('Hola, soy el thread número uno')
	logging.info('Estoy a la espera de la señal')

	# Con event wait indicamos que se detenga el thread
	# Se reanudará cuando reciba una señal
	event.wait()

	logging.info('La señal fue dada, la bandera es True')


def thread_2(event):

	while not event.is_set():
		logging.info('A la espera de la señal')
		time.sleep(0.5)

if __name__ == '__main__':
	
	event = threading.Event()
	# Bandero = True o False

	thread1 = threading.Thread(target=thread_1, args=(event, ))
	thread2 = threading.Thread(target=thread_2, args=(event, ))

	thread1.start()
	thread2.start()

	# Simulamos que el thread principal está relizando un tarea compleja
	time.sleep(3)

	# Con el método set envíamos la señal para que el thread continue
	event.set()

# Podemos volver a colocar la bandera en True
#	event.clear()
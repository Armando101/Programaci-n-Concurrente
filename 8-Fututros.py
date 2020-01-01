import time
import threading
import logging

# Importamos la clase Future
from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Futures
# Un Future es la abstracción de un futureado
# Un Future representa un valor eventual
# En JavaScript se les conoce como promesas

# Este callback debe recibir un parámetro que hace referencia al futuro
def callback_future(future):
	logging.info('Hola, soy un callback que se ejecuta cuando el futuro posee un valor')
	logging.info(f'El futuro es: {future.result()}')


if __name__ == '__main__':

# Generamos el future
	future = Future()
	future.add_done_callback(callback_future)
	future.add_done_callback(
			lambda future: logging.info('Hola, soy una lambda!')
		)


# Simulamos tareas complejas
	logging.info('Comenzamos una tarea muy compleja!!!')

	time.sleep(2)

	logging.info('Terminamos la tarea compleja')

# Asignamos un valor
	logging.info('Vamos a asignar un valor al futuro')

	# Este método recibe cualquier objeto, string, tupla, diccionario, etc.
	future.set_result("Armando Rivera")

	# Cuando el future ya posee un valor se van a ejecutar todos los callback's asociados a dicho futuro
	logging.info('El future ya posee un valor')
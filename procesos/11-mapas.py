import time
import logging
from multiprocessing import Pool

logging.basicConfig(level = logging.DEBUG, format = '%(processName)s %(message)s')

def is_even(number):
	time.sleep(1)
	return number % 2 == 0

def show_results(results):
	logging.info(f'El resultado es: {results}')

if __name__ == '__main__':
	with Pool(processes=2) as executor:
		numbers = [number for number in range(1, 11)]

		# El método executor.map devuelve un valor hasta que todos los valores se hayan pasado a la función
		# Esto es un problema cuando la función requiere un gran costo computacional ya que no devolverá nada hasta que todos los elementos hayan sido pasados a la función.

		# list_result = executor.map(is_even, numbers)
		
		# Para evitar eso usamos el método map_async
		# Dicha función nos devuelve un objeto
		# Podemos agregar un callback a la función map_async
		# Esto es una función que se ejecutará cuando map_result posea un valor

		map_result = executor.map_async(is_even, numbers, callback=show_results)

		# Indicamos que el proceso espere hasta que todos los elementos estén listos. También podemos programar un tiempo máximo de espera con timeout

		#map_result.wait(timeout = 1)
		
		logging.info('Vamos a esper hasta que los resultados esten listos')

		map_result.wait()

		logging.info(f'El resultado es: {map_result.get()}')
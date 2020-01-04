import time
import logging
import threading

from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level = logging.DEBUG, format='%(threadName)s : %(message)s')

"""
Generar threads es algo costoso por lo que debemos evitar crear threads de manera indiscriminadada.

Mediante una piscina podemos generar N cantidad de threads, estos threads estarán bajo demanda, es decir, se van a ejecutar cuando se necesiten.
Estos threads los podemos reutilizar para evitar crear threads nuevos.

Para trabajar con la piscina de threads necesitamos la libreria ThreadPoolExecutor
"""
def math_operation(number1, number2):

	time.sleep(1)

	result = number1 + number2
	logging.info(f'Resultado de {number1} + {number2} = {result}')

if __name__ == '__main__':
	
	# Indicamos mediante el parámetro max_workers el número de threads que queremos en la piscina
	# También es posible agregar un prefijo a los threads
	executor = ThreadPoolExecutor(max_workers=25, thread_name_prefix='Piscina')

	# Para generar un thread lo hacemos de la siguiente manera
	# Mediante el método submit indicamos la función que se ejecutará en segundo plano y pasamos los argumentos

	executor.submit(math_operation, 10, 20)

	# Si ejecutamo una tarea pero no hay threads para realizarla, ésta se agenda y se le asigna al primer thread que se libere

	for _ in range(0, 100):
		executor.submit(math_operation, 10, 20)

	# Con el método shutdown apagamos la piscina, esto significa que no podemos usar el método submit después de este.
	executor.shutdown()

"""
	# Este bloque no es eficiente ya que estamos generando 100 threads, esto resulta en que sale más costoso generar los threads que realizar la operación matemática

	for _ in range(0, 1000):
		thread = threading.Thread(target=math_operation, args=(10, 20))
		thread.start()
""" 

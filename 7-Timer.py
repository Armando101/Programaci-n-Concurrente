import logging
import threading

logging.basicConfig(level = logging.DEBUG, format='%(message)s')

# El módulo threading nos ofrece la clase Timer
# La clase Timer nos permite especificar el momento en el que queremos que un callback se ejecute
# La clase Timer nos permite definir callbacks a partir de periodos de tiempo

# La clase Timer recibe dos argumentos
# El primero es un número que hace referencia a la cantidad de tiempo que debe esperar el callback para ser ejecutado en segundos
# El segundo argumento es el callback a ejecutar


def callback():
	logging.info('Hola, soy un callback que no se ejecuta de forma inmediata')

if __name__ == '__main__':
	thread = threading.Timer(3, callback)
	thread.start()

	logging.info('Hola soy el thread principal')
	logging.info('Estamos a la espera de la ejeción del callback')

# A través de la clase Timer podemos programar el momento en que un callback será ejecutado
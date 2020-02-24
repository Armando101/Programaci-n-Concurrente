from time import sleep
import logging
import multiprocessing

logging.basicConfig(level = logging.DEBUG, format = '%(processName)s %(message)s')

"""
Otra forma de comunicar procesos en con manager
Esto se logra mediante un namespace
Vamos a trabajar bajo un contexto
"""

# Lo primero que hacemos es definir un objeto de tipo Manager
# Después definimos un namespace
# Con el namespace vamos a definir todas las variables con las que queremos que nuestros procesos compartan

def get_valor(namespace):
	while namespace.proteco is None:
		logging.info('Proteco no posee valor alguno!')
		sleep(0.5)
	else:
		logging.info(namespace.proteco)
		logging.info(namespace.prueba_de_nueva_variable)

def set_valor(namespace):
	sleep(4)
	namespace.proteco = 'Programa de Tecnología en Cómputo'
	namespace.prueba_de_nueva_variable = False


if __name__ == '__main__':
	manager = multiprocessing.Manager()
	namespace = manager.Namespace()

	# Ahora podemos definir las variables que queremos que compartan
	namespace.proteco = None
	namespace.prueba_de_nueva_variable = True

	process1 = multiprocessing.Process(target=get_valor, args=(namespace, ))
	process2 = multiprocessing.Process(target=set_valor, args=(namespace, ))

	process1.start()
	process2.start()
	
	process1.join()
	process2.join()

import logging

logging.basicConfig(
		level = logging.DEBUG,
		format = '%(thread)s %(threadName)s : %(message)s'
	)

# Todos los procesos crear un nuevo thread, el thread principal
# Este thread principal se puede ver al imprimir el mensaje

if __name__ == '__main__':
	logging.debug('Hola me encuentro en el thread principal!!')


#################### Dormir un thread ###############
# Le indicamos al sistema que este thread no estará activo en un cierto tiempo
# Damos paso a que otros threads ocupen el espacio del thread dormido

# Necesitamos los siguientes módulos
import time
import threading

# La función sleep recibe un parámetro en segundos
# sleep(segundos)

def task():
	logging.info('Nos encontramos ejecutando una nueva tarea')
	time.sleep(2)
	logging.info('Tarea finalizada')


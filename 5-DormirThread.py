#################### Dormir un thread ###############

# Le indicamos al sistema que este thread no estará activo en un cierto tiempo
# Damos paso a que otros threads ocupen el espacio del thread dormido

# Necesitamos los siguientes módulos
import time
import threading
import logging

logging.basicConfig(
		level = logging.DEBUG,
		format = '%(thread)s %(threadName)s : %(message)s'
	)

# Para dormir un thread nos apoyamos de la función time 
# Podemos dormir un thread que hayamos creado o el thread principal	
# La función sleep recibe un parámetro en segundos
# sleep(segundos)

def task():
	logging.info('Nos encontramos ejecutando una nueva tarea')
	time.sleep(2)
	logging.info('Tarea finalizada')


if __name__ == '__main__':

#	Dormir un thread creado por nosotros
#	thread = threading.Thread(target = task)
#	thread.start()

#	Dormir el thread principal
#	Podemos simular un reloj digital
	contador = 0
	while True:
		time.sleep(1)
		contador += 1
		logging.info(f'Tiempo transcurrido: {contador} segundos')


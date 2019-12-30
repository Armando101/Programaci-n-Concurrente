# Logging es un módulo que nos permite testear las aplicaciones
# Este módulo nos ofrece 5 tipos de mensaje
# Debug(10), Info(20), Warning(30), Error(40), Critical(50)
# Eĺ módulo logging está configurado para mostrar únicamente mensajes de nivel 30 o superior

import logging

# Podemos cambiar a configuración de logging para que muestre los demás mensajes
logging.basicConfig(

	# Indico que quiero mostrar todos los mensajes desde el nivel 10
 	level = 10,	
#	level=logging.DEBUG,	# Esta línea es equivalente a la anterior
	
	# Podemos colocar un formato deseado con format
	format ='%(message)s - %(levelname)s - %(lineno)s- %(thread)s - %(threadName)s - %(process)s - %(processName)s', 
	
	# Definimos un formato de fecha
	datefmt = '%H:%M:%S',

	# Puedo indicar un archivo en el cual quiero que se guarden los mensajes
#	filename = 'messages.txt'
	)

# filename: indica el nombre del archivo
# asctiem: indica la fecha actual
# messages: muestra el mensaje
# funcName: muestra el nombre de la función que está siendo ejecutada
# levelname: muestra el nivel del mensaje
# lineno: número de línea ejecutada
# modules: muestra el módulo ejeutado
# name: nombre de logging
# thread: muestra el thread
# threadName: muestra el nombre del thread
# process: muestra	el proceso
# processName: muestra el nombre del proceso


def mis_mensajes():
	logging.debug('Este es un mensaje de tipo Debug')
	logging.info('Este es un mensaje de tipo Info')
	logging.warning('Este es un mensaje de tipo Warning')
	logging.error('Este es un mensaje de tipo Error')
	logging.critical('Este es un mensaje de tipo Critical')

if __name__ == '__main__':
	mis_mensajes()
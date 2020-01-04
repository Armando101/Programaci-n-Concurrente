import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

BALANCE = 100

# Se puede dar el caso debido a una mala implementación que se intente acceder a un recurso compartido más de una vez sin antes ejecutar el método release, esto es ejecutar dos veces el método acquire sin antes dejecutar el release, para evitar eso usamos un objeto RLock en lugar de Lock

# RLock puede adquirri un recurso compartido varias veces por el mismo thread
# Si adquirimos N veces un recurso también necesitamos liberarlo N veces

# Lock perimte adquier una vez el recurso compartido
# RLock permite adquirir el recurso N veces

lock = threading.RLock()

if __name__ == '__main__':
	
	lock.acquire()
	lock.acquire()

	BALANCE -= 10

	lock.release()
	lock.release()

	logging.info(f'Finalizamos el thread principal con el balance {BALANCE}')
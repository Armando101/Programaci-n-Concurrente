import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')

BALANCE = 0

# Los threads se pueden comunicar entre sí
# Si hacemos un depósito de 100,000 y retiramos 100,000 el balance es de 0


# Si hacemos un depósito de 1,000,000 y retiramos 1,000,000 el balance ya no es de 0, a este error se le conoce como RACE CONDITION
# RACE CONDITION es un error que ocurre cuando más de un thread intenta correr y modificar un espacio de memoria compartido
# En este caso dos threads intentan acceder a una misma variable.
# Este error ocurre porque las tareas se ejecutan de manera concurrente

# Para solucionar este error nos aseguramos de que las secciones críticas se ejecuten una vez por cada thread, es decir, que primero se ejecute un thread y después el otro

# Para lograr que sólo un thread a la vez pueda acceder y modificar el recurso compartido nos apoyaremos de un recurso llamado lock
# Esto es "ponerle un candado" a la sección critica
lock = threading.Lock()

# Con la función acquire hacemos que los threads no se ejecuten a la vez en la función critical
# Esto es como una cabina telefónica, no podemos usar la cabina si está siendo usada
# Un thread no podrá modificar la variable si otro thread la está modificando
# Una vez que el thread ya terminó de usar la variable, la "liberamos con la función release", esto hace que deje la sección libre para que otro thread la utilice

def depositos():
	global BALANCE

	for _ in range(0, 10000):
		lock.acquire()
		BALANCE +=1	# Sección crítica
		lock.release()

# También es posible usar lock con el contexto with de la siguiente manera
def retiros():
	global BALANCE

	for _ in range(0, 10000):
		with lock:
			BALANCE -=1 # Sección crítica

# Otra forma de utilizar los lock es con try catch finally
def depositos_2():
	global BALANCE
	for _ in range(0,10000):
		try:
			lock.acquire()
			BALANCE += 1
		finally:
			lock.release()

if __name__ == '__main__':
	thread1 = threading.Thread(target=depositos)
	thread2 = threading.Thread(target=retiros)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	logging.info(f'El valor final del balance es: {BALANCE}')
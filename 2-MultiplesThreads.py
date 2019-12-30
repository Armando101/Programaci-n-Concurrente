import threading

def executor_a(id=0):
	for x in range(0,10):
		print(f"Hola, soy el thread {id} iteración {x}")


def executor_b(id=0):
	for x in range(0,10):
		print(f"Hola, soy el thread {id} iteración {x}")


def executor_c(id=0):
	for x in range(0,10):
		print(f"Hola, soy el thread {id} iteración {x}")

# Podemos utilizar múltiples Threads en un script
# Podemos pasar parámetros a las funciones mediante una lista, tupla o diccionario
# Lista: se colocan los valores dentro de corchetes
# Tupla: se colocan los valores dentro	de paréntesis finalizando con una coma
# Diccionario: se coloca como llave el nombre del parámetro y el valor del parámetro
thread_a = threading.Thread(target = executor_a, args = [1])
thread_b = threading.Thread(target = executor_b, args = (2,))
thread_c = threading.Thread(target = executor_c, kwargs = {'id':3})

thread_a.start()
thread_b.start()
thread_c.start()


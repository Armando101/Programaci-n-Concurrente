"""
Creación de threads
"""

# Utilizamos la api randomuser para hacer peticiones a usuarios aleatorios
import requests
import threading 	# Módlo para hacer threads

def get_name():
	response = requests.get('https://randomuser.me/api/')
	if response.status_code == 200:
		
		results = response.json().get('results')
		name = results[0].get('name').get('first')

		print(name)

# target recibe como parámetro aquella función que queremos ejecutar de manera concurrente

if __name__ == '__main__':
	
	for _ in range(0,20):
#	 Llamada secuencial
#		get_name()

#	Llamdada concurrente
		thread = threading.Thread(target = get_name)
		thread.start()	# Indicamos que las instrucciones se ejecuten de manera concurrente
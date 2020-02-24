import time
import logging
#from current.futures import ProcessPoolExecutor
# Es recomendable usar la función ProcessPoolExecutor en lugar de Pool
# Esto porque el módulo ProcessPoolExecutor fue pensado para ser ejecutado de forma paralela y Pool no
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

def is_even(number):
	return number%2==0

if __name__ == '__main__':
	with Pool(processes=2) as executor:
		# La función executor.apply retorna lo que la función retorna
		# Es importante señalar que apply se ejecuta secuencialmente
		result = executor.apply(is_even, args=(10, ))
		logging.info(f'El resultado es: {result}')
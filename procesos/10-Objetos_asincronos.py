from time import sleep
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

def is_even(number):
	sleep(3)
	return number%2==0

if __name__ == '__main__':
	with Pool(processes=2) as executor:
		# El método apply_async ejecuta la función de manera asincrona
		apply_result = executor.apply_async(is_even, args=(10,))

		logging.info('Esperamos momentaneamente hasta que apply_result contenga un valor')

		# Con el método wait indicamos que detenga el proceso padre hasta que apply_result contenga un valor 
		apply_result.wait()

		logging.info('apply_result ha finalizado')

		logging.info(f'El resultado es: {apply_result.get()}')

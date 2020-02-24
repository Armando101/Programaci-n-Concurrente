import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

# Pipes
# Publisher
# Subsciber

class Publisher(multiprocessing.Process):
	def __init__(self, connnection):
		self.connnection = connnection
		multiprocessing.Process.__init__(self)

	def run(self):
		logging.info('Hola, nos encontramos el el proceso Publisher')

		for x in range(20):
			self.connnection.send(f'Hola desde el proceso Publisher, con el valor {x}')
			time.sleep(0.5)

		self.connnection.send(None)
		self.connnection.close()

		logging.info('Conección cerrada para publisher')

class Subscriber(multiprocessing.Process):
	def __init__(self, connnection):
		self.is_alive=True
		self.connnection = connnection
		multiprocessing.Process.__init__(self)

	def run(self):
		logging.info('Hola, nos encontramos el el proceso Subscriber')

		while self.is_alive:
			result = self.connnection.recv()
			
			self.is_alive = result is not None

			logging.info(result)
		else:
			self.connnection.close()

			logging.info('Conección cerrada para subscriber')
			
if __name__ == '__main__':

	connnection1, connection2 = multiprocessing.Pipe()

	publisher = Publisher(connnection1)
	subscriber = Subscriber(connection2)

	publisher.start()
	subscriber.start()


import multiprocessing
import logging

logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')

def deposit(namespace, lock):
	for _ in range(1, 100000):
		lock.acquire()
		namespace.balance += 1
		lock.release()


def withdraw(namespace, lock):
	for _ in range(1, 100000):
		with lock:
			namespace.balance -= 1

if __name__ == '__main__':
	manager = multiprocessing.Manager()

	lock = manager.Lock()

	namespace = manager.Namespace()
	namespace.balance = 0

	process1 = multiprocessing.Process(target=deposit, args=(namespace, lock))
	process2 = multiprocessing.Process(target=withdraw, args=(namespace, lock))

	process1.start()
	process2.start()

	process1.join()
	process2.join()

	logging.info(f'El balance final es: {namespace.balance}')
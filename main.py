import threading
import os
from multiprocessing.connection import Listener
from pyfiglet import Figlet
from colorama import Fore, Style
from function.plural import plural
from function.worker import worker
from function.clLine import clLine
from function.statistic import statistic

if __name__ == "__main__":

	try:
		address = ('localhost', 6872)
		listener = Listener(address)
	except Exception as e:
		print(f"Server error: {e}")

	workerNumber = 10

	for i in range(workerNumber):
		try:
			t = threading.Thread(target=worker)
			t.start()
		except Exception as e:
			clLine()
			print(f"Thread error: {Fore.RED}{e}{Style.RESET_ALL}")

tempLine = []

while True:
	width, height = os.get_terminal_size()

	conn = listener.accept()
	listener.last_accepted
	msg = conn.recv()

	os.system("cls || clear")

	print(f"{Fore.LIGHTYELLOW_EX}{Figlet(font='small').renderText('BruteInfiniteCraft')}{Style.RESET_ALL}")
	statistic()
	print("\n\n")

	tempLine.append(msg)
	# clLine()
	# print(msg)

	print("\n".join(tempLine[-(height-10):]))


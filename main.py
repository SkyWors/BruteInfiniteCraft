import threading
import os
import socket
from pyfiglet import Figlet
from colorama import Fore, Style
from function.worker import worker
from function.clLine import clLine
from function.statistic import statistic

if __name__ == "__main__":

	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket.bind(("127.0.0.1", 65432))
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

	server_socket.listen()
	conn, addr = server_socket.accept()
	msg = conn.recv(1024)

	os.system("cls || clear")

	print(f"{Fore.LIGHTYELLOW_EX}{Figlet(font='small').renderText('BruteInfiniteCraft')}{Style.RESET_ALL}")
	statistic()
	print("\n\n")

	tempLine.append(msg.decode(encoding="utf-8"))

	print("\n".join(tempLine[-(height-10):]))


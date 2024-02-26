import threading
import sys
from pyfiglet import Figlet
from colorama import Fore, Style
from function.plural import plural
from function.worker import worker
from function.clLine import clLine

if __name__ == "__main__":
	workerNumber = 1

	print(f"{Fore.LIGHTYELLOW_EX}{Figlet(font='small').renderText('BruteInfiniteCraft')}{Style.RESET_ALL}")

	print(f"{Fore.LIGHTBLACK_EX}Starting {workerNumber} worker{plural(workerNumber)}...{Style.RESET_ALL}\n")

	for i in range(workerNumber):
		try:
			t = threading.Thread(target=worker)
			t.start()
		except Exception as e:
			clLine()
			print(f"Thread error: {Fore.RED}{e}{Style.RESET_ALL}")

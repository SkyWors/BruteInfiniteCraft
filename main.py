import mysql.connector
import requests
import threading
from colorama import Fore, Style

def isAlreadyInDB(value):
	if value:
		return "_"
	else:
		return f"{Fore.GREEN}+{Style.RESET_ALL}"

def isNewItem(value):
	if value:
		return f"{Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}"
	else:
		return "_"

def colorResult(isExist, isNew, item):
	if isNew:
		return f"{Fore.LIGHTYELLOW_EX}{item}"
	else:
		if isExist:
			return f"{Style.RESET_ALL}{item}"
		else:
			return f"{Fore.GREEN}{item}"

def craft(itemId1, item1, itemId2, item2):
	try:
		database = mysql.connector.connect(host="localhost", user="root", password="", database="bruteinfinitecraft", charset="utf8mb4")
		cursor = database.cursor()

		response = requests.get(
			f"https://neal.fun/api/infinite-craft/pair?first={item1}&second={item2}",
			headers={
				"accept": "*/*",
				"accept-language": "fr-FR,fr;q=0.9",
				"cache-control": "no-cache",
				"pragma": "no-cache",
				"Referer": "https://neal.fun/infinite-craft/",
				"Referrer-Policy": "strict-origin-when-cross-origin",
				"sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
				"sec-ch-ua-mobile": "?0",
				"sec-ch-ua-platform": '"Windows"',
				"sec-fetch-dest": "empty",
				"sec-fetch-mode": "cors",
				"sec-fetch-site": "same-origin",
				"User-Agent": "Mozilla/5.0 (Linux i546 x86_64; en-US) AppleWebKit/537.10 (KHTML, like Gecko) Chrome/47.0.1707.389 Safari/603"
			}
		)

		if response.ok:
			data = response.json()

			# Nothing is not an item
			if data['result'] == "Nothing":
				print(f"[{Fore.RED}X{Style.RESET_ALL}] [{Fore.RED}X{Style.RESET_ALL}] {item1} + {item2} = {Fore.RED}Nothing find.{Style.RESET_ALL}")
				return

			cursor.execute(f"SELECT name FROM item WHERE name = '{data['result']}'")
			isExist = cursor.fetchone()

			print(f"[{isAlreadyInDB(isExist)}] [{isNewItem(data['isNew'])}] {item1} + {item2} = {colorResult(isExist, data['isNew'], data['result'])} {data['emoji']}{Style.RESET_ALL}")

			if (isExist):
				return
			else:
				cursor.execute(f"INSERT INTO item (name, symbole, isNew) VALUES ('{data['result']}', '{data['emoji']}', {data['isNew']})")
				database.commit()

				cursor.execute(f"SELECT id FROM item WHERE name = '{data['result']}'")
				idResult = cursor.fetchone()

				cursor.execute(f"INSERT INTO craft (idItem1, idItem2, idResult) VALUES ({itemId1}, {itemId2}, {idResult[0]})")
				database.commit()
		else:
			print(f"Crafting failed: {Fore.RED}{response.status_code} {response.reason}{Style.RESET_ALL}")
	except Exception as e:
		print(f"Craft error: {Fore.RED}{e}{Style.RESET_ALL}")

def worker():
	database = mysql.connector.connect(host="localhost", user="root", password="", database="bruteinfinitecraft", charset="utf8mb4")
	cursor = database.cursor()

	while True:
		cursor.execute("SELECT id, name FROM item ORDER BY RAND() LIMIT 1")
		request1 = cursor.fetchall()
		cursor.execute("SELECT id, name FROM item ORDER BY RAND() LIMIT 1")
		request2 = cursor.fetchall()

		tempId = []
		tempName = []
		for value in request1:
			tempId.append(value[0])
			tempName.append(value[1])
		for value in request2:
			tempId.append(value[0])
			tempName.append(value[1])

		craft(tempId[0], tempName[0], tempId[1], tempName[1])

workerNumber = 1

print("\n  = BruteInfiniteCraft =\n")
print(f"Starting {workerNumber} workers...")
for i in range(workerNumber):
	try:
		t = threading.Thread(target=worker)
		t.start()
	except Exception as e:
		print(f"Thread error: {Fore.RED}{e}{Style.RESET_ALL}")

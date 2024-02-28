import mysql.connector
import requests
import os
import socket
from dotenv import load_dotenv
from colorama import Fore, Style
from function.indicator import indicator
from function.colorResult import colorResult
from function.clLine import clLine

load_dotenv()

def craft(itemId1, item1, itemId2, item2):
	try:
		try:
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client_socket.connect(("127.0.0.1", 6583))
		except Exception as e:
			clLine()
			print(f"Connexion error: {Fore.RED}{e}{Style.RESET_ALL}")

		database = mysql.connector.connect(host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), database=os.getenv("MYSQL_DB"), charset="utf8mb4")
		cursor = database.cursor()

		try:
			response = requests.get(
				f"https://neal.fun/api/infinite-craft/pair?first={item1}&second={item2}",
				headers={
					"Referer": "https://neal.fun/infinite-craft/",
					"User-Agent": "Mozilla/5.0 (Linux i546 x86_64; en-US) AppleWebKit/537.10 (KHTML, like Gecko) Chrome/47.0.1707.389 Safari/603",
					'accept-language': 'en-US,en;q=0.9',
			        'sec-ch-ua': '"Not(A:Brand";v="24", "Chromium";v="122"'
				},
			)

			if response.ok:
				data = response.json()

				# Nothing is not an item
				if data['result'] == "Nothing":
					client_socket.sendall(f"[{Fore.RED}x{Style.RESET_ALL}] {item1} + {item2} = {Fore.RED}Nothing found.{Style.RESET_ALL}".encode(encoding="utf-8"))

					cursor.execute(f"INSERT INTO craft (idItem1, idItem2) VALUES ({itemId1}, {itemId2})")
					database.commit()
					return

				cursor.execute(f"SELECT name FROM item WHERE name = '{data['result']}'")
				isExist = cursor.fetchone()

				client_socket.sendall(f"[{indicator(isExist, data['isNew'])}] {item1} + {item2} = {colorResult(isExist, data['isNew'], data['result'])} {data['emoji']}{Style.RESET_ALL}".encode(encoding="utf-8"))

				if (isExist):
					cursor.execute(f"SELECT id FROM item WHERE name = '{data['result']}'")
					idResult = cursor.fetchone()

					cursor.execute(f"INSERT INTO craft (idItem1, idItem2, idResult) VALUES ({itemId1}, {itemId2}, {idResult[0]})")
					database.commit()
					return
				else:
					cursor.execute(f"INSERT INTO item (name, symbole, isNew) VALUES ('{data['result']}', '{data['emoji']}', {data['isNew']})")
					database.commit()

					cursor.execute(f"SELECT id FROM item WHERE name = '{data['result']}'")
					idResult = cursor.fetchone()

					cursor.execute(f"INSERT INTO craft (idItem1, idItem2, idResult) VALUES ({itemId1}, {itemId2}, {idResult[0]})")
					database.commit()
			else:
				clLine()
				client_socket.sendall(f"Crafting failed: {Fore.RED}{response.status_code} {response.reason}{Style.RESET_ALL}".encode(encoding="utf-8"))
		except Exception as e:
			clLine()
			client_socket.sendall(f"API error: {Fore.RED}{e}{Style.RESET_ALL}".encode(encoding="utf-8"))
	except Exception as e:
		clLine()
		client_socket.sendall(f"Craft error: {Fore.RED}{e}{Style.RESET_ALL}".encode(encoding="utf-8"))

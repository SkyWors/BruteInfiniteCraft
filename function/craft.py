import mysql.connector
import requests
import os
from dotenv import load_dotenv
from colorama import Fore, Style
from function.indicator import indicator
from function.colorResult import colorResult

load_dotenv()

def craft(itemId1, item1, itemId2, item2):
	try:
		database = mysql.connector.connect(host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), database=os.getenv("MYSQL_DB"), charset="utf8mb4")
		cursor = database.cursor()

		try:
			response = requests.get(
				f"https://neal.fun/api/infinite-craft/pair?first={item1}&second={item2}",
				headers={
					"Referer": "https://neal.fun/infinite-craft/",
					"User-Agent": "Mozilla/5.0 (Linux i546 x86_64; en-US) AppleWebKit/537.10 (KHTML, like Gecko) Chrome/47.0.1707.389 Safari/603"
				},
			)

			if response.ok:
				data = response.json()

				# Nothing is not an item
				if data['result'] == "Nothing":
					print(f"[{Fore.RED}x{Style.RESET_ALL}] {item1} + {item2} = {Fore.RED}Nothing found.{Style.RESET_ALL}")

					cursor.execute(f"INSERT INTO craft (idItem1, idItem2) VALUES ({itemId1}, {itemId2})")
					database.commit()
					return

				cursor.execute(f"SELECT name FROM item WHERE name = '{data['result']}'")
				isExist = cursor.fetchone()

				print(f"[{indicator(isExist, data['isNew'])}] {item1} + {item2} = {colorResult(isExist, data['isNew'], data['result'])} {data['emoji']}{Style.RESET_ALL}")

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
				print(f"Crafting failed: {Fore.RED}{response.status_code} {response.reason}{Style.RESET_ALL}")
		except Exception as e:
			print(f"API error: {Fore.RED}{e}{Style.RESET_ALL}")
	except Exception as e:
		print(f"Craft error: {Fore.RED}{e}{Style.RESET_ALL}")

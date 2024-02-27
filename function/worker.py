import mysql.connector
import os
from dotenv import load_dotenv
from colorama import Fore, Style
from function.plural import plural
from function.craft import craft
from function.clLine import clLine

load_dotenv()

def worker():
	try:
		database = mysql.connector.connect(host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), database=os.getenv("MYSQL_DB"), charset="utf8mb4")
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

			cursor.execute(f"SELECT * FROM craft WHERE idItem1 = {tempId[0]} AND idItem2 = {tempId[1]}")
			isCraftExist1 = cursor.fetchone()
			cursor.execute(f"SELECT * FROM craft WHERE idItem1 = {tempId[1]} AND idItem2 = {tempId[0]}")
			isCraftExist2 = cursor.fetchone()

			if isCraftExist1:
				continue
			if isCraftExist2:
				continue

			craft(tempId[0], tempName[0], tempId[1], tempName[1])
	except Exception as e:
		clLine()
		print(f"Worker error: {Fore.RED}{e}{Style.RESET_ALL}")

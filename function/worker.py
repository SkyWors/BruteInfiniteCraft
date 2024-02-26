import mysql.connector
import os
import threading
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

			cursor.execute(f"SELECT count(*) FROM item")
			itemCount = cursor.fetchone()
			database.commit()
			cursor.execute(f"SELECT count(*) FROM craft")
			recipeCount = cursor.fetchone()
			database.commit()
			cursor.execute(f"SELECT count(*) FROM item WHERE isNew = 1")
			firstDiscoveryCount = cursor.fetchone()
			database.commit()

			print(f"    {Fore.LIGHTBLACK_EX}Workers : {threading.active_count()-1}   🧱Item{plural(itemCount[0])}: {Fore.BLUE}{itemCount[0]}   {Fore.LIGHTBLACK_EX}📄Recipe{plural(recipeCount[0])}: {Fore.BLUE}{recipeCount[0]}   {Fore.LIGHTBLACK_EX}⭐First discovery: {Fore.BLUE}{firstDiscoveryCount[0]}{Style.RESET_ALL}", end="\r")
	except Exception as e:
		clLine()
		print(f"Worker error: {Fore.RED}{e}{Style.RESET_ALL}")

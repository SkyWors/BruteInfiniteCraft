import mysql.connector
import os
from dotenv import load_dotenv
from function.craft import craft

load_dotenv()

def worker():
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
			return
		if isCraftExist2:
			return

		craft(tempId[0], tempName[0], tempId[1], tempName[1])

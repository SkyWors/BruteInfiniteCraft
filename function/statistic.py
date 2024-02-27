import mysql.connector
import os
import threading
import time
from colorama import Fore, Style
from function.plural import plural

def statistic():
	database = mysql.connector.connect(host=os.getenv("MYSQL_HOST"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), database=os.getenv("MYSQL_DB"), charset="utf8mb4")
	cursor = database.cursor()

	cursor.execute(f"SELECT count(*) FROM item")
	itemCount = cursor.fetchone()
	cursor.execute(f"SELECT count(*) FROM craft")
	recipeCount = cursor.fetchone()
	cursor.execute(f"SELECT count(*) FROM item WHERE isNew = 1")
	firstDiscoveryCount = cursor.fetchone()

	print(f"{Fore.LIGHTBLACK_EX}Workers: {threading.active_count()-1}   🧱Item{plural(itemCount[0])}: {Fore.BLUE}{itemCount[0]}   {Fore.LIGHTBLACK_EX}📄Recipe{plural(recipeCount[0])}: {Fore.BLUE}{recipeCount[0]}   {Fore.LIGHTBLACK_EX}⭐First discovery: {Fore.BLUE}{firstDiscoveryCount[0]}{Style.RESET_ALL}", end="\r")


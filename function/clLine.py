import os

width, height = os.get_terminal_size()

def clLine():
	clLine = []
	for i in range(width):
		clLine.append(" ")
	print("".join(clLine), end="\r")

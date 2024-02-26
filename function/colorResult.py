from colorama import Fore, Style

def colorResult(isExist, isNew, item):
	if isNew:
		return f"{Fore.LIGHTYELLOW_EX}{item}"
	else:
		if isExist:
			return f"{Style.RESET_ALL}{item}"
		else:
			return f"{Fore.GREEN}{item}"

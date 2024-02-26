from colorama import Fore, Style

def indicator(isExist, isNew):
	if isNew:
		return f"{Fore.LIGHTYELLOW_EX}*{Style.RESET_ALL}"
	else:
		if isExist:
			return " "
		else:
			return f"{Fore.GREEN}+{Style.RESET_ALL}"

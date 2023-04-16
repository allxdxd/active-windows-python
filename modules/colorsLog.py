from colorama import init, Fore

init()

def errorlog(text, _end = '\n'):
    print(Fore.RED + str(text), end= _end)

def log(text, _end = '\n'):
    print(Fore.YELLOW + str(text), end= _end)

def greenlog(text, _end = '\n'):
    print(Fore.GREEN + str(text), end= _end)

def bluelog(text, _end = '\n'):
    print(Fore.CYAN + str(text), end= _end)
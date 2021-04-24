import sys
import socket
import ipaddress
import requests
from time import sleep
from colorama import Fore



def GetTargetAddress(target, method):
    if method == "SMS":
        if target.startswith("+"):
            target = target[1:]
        return target    



def InternetConnectionCheck():
    try:
        requests.get("https://google.com", timeout=6)
    except:
        print(
            f"{Fore.LIGHTRED_EX}[!] {Fore.LIGHTBLUE_EX}Твое устройство не подключено к интернету{Fore.RESET}"
        )
        sys.exit(1)

import os
import sys
import platform
from time import ctime
from colorama import Fore



def CriticalError(message, error):
    print(f"""
    {Fore.YELLOW}:=== Critical error:
    {Fore.GREEN}Сообщение: {message}.
    {Fore.RED}Ошибка: {error}
    {Fore.LIGHTRED_EX}:=== Информация о питоне:
    {Fore.LIGHTRED_EX}Версия питона: {platform.python_version()}
    {Fore.LIGHTRED_EX}Сборка питона: {'{}, DATE: {}'.format(*platform.python_build())}
    {Fore.LIGHTRED_EX}Копилятор питона: {platform.python_compiler()}
    {Fore.LIGHTRED_EX}Расположение скрипта: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.LIGHTRED_EX}Текущее расположение: {os.getcwd()}
    {Fore.CYAN}:=== Информация о системе:
    {Fore.LIGHTRED_EX}Система: {platform.system()}
    {Fore.LIGHTRED_EX}Выпуск: {platform.release()}
    {Fore.LIGHTRED_EX}Версия: {platform.version()}
    {Fore.LIGHTRED_EX}Архитектура: {'{} {}'.format(*platform.architecture())}
    {Fore.LIGHTRED_EX}Процессор: {platform.processor()}
    {Fore.LIGHTRED_EX}Машина: {platform.machine()}
    {Fore.LIGHTRED_EX}Узел: {platform.node()}
    {Fore.LIGHTRED_EX}Время: {ctime()}
    """)
    sys.exit(5)

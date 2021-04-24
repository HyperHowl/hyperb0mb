import json
import random
import string

mails = (
    "mail.ru",
    "ya.ru",
    "yandex.com",
    "yandex.ua",
    "yandex.ru",
    "gmail.com",
)



def random_service(list):
    return random.choice(list)



def random_name():
    with open("tools/SMS/names.json", "r") as names:
        names = json.load(names)["names"]
    return random.choice(names)



def random_suffix(int_range=4):
    numbers = []
    for _ in range(int_range):
        numbers.append(str(random.randint(1, 9)))
    return "".join(numbers)


def random_email():
    return random_name() + random_suffix() + "@" + random.choice(mails)



def random_password():
    return random_name() + random_suffix(int_range=10)



def random_token():
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(random.randint(20, 50)))


def random_useragent():
    with open("tools/SMS/user_agents.json", "r") as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)

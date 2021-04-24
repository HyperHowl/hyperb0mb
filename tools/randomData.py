import json
import random



def random_useragent():
    with open("tools/L7/user_agents.json", "r") as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)

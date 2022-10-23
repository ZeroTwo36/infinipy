from infinipy.fetch import fetch
from infinipy.abc import User, Bot
API_URL = "https://api.infinitybotlist.com"


def fetch_bot(id):
    return Bot(**fetch(f"{API_URL}/bots/{id}").json())


def fetch_user(id):
    return User(**fetch(f"{API_URL}/users/{id}").json())


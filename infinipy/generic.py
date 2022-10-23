from infinipy.fetch import fetch
from infinipy.abc import Bot, Announcement
from typing import Generator
API_URL = "https://api.infinitybotlist.com"


def all_bots() -> Generator[Bot]:
    f = fetch(f"{API_URL}/bots/all")
    for r in f.json()["bots"]:
        yield Bot(**r)

def announcements(user=""):
    a = fetch(f"{API_URL}/announcements", headers={"Authorization": f"User {user}"})
    return Announcement(**a.json())

from infinipy.abc import Bot
from infinipy.core import fetch_bot
from infinipy.fetch import fetch
from threading import Thread
from typing import Union, overload
import time

class AutoPoster:
    @overload
    def __init__(self, bot: Bot):...

    @overload
    def __init__(self, bot: int):...

    def __init__(self, bot):
        if isinstance(bot, Bot):
            self.bot = Bot
        else:
            self.bot = fetch_bot(bot)
        self.__subprocess = Thread(target=self.__start__)
        self.alive = True

    def start(self, auth):
        self.auth = auth
        self.__subprocess.start()

    def __start__(self):
        while self.alive:
            x = fetch(f"https://japi.rest/discord/v1/application/{self.bot.id}")
            guild_count = x["data"]["bot"]["approximate_guild_count"]
            shard_count = 1
            self.bot.set_stats(guild_count, shard_count, self.auth)
            time.sleep(120)

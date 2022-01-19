import imp
from .core import *
import time
import threading


class AutoStatsUpdater:
    def __init__(self,bot,api_key, interval:int=120) -> None:
        """Automatically pushes a discord.py bot's stats to the API.

        Difference to Sync/AsyncAPISession? This Class automatically updates stats every
        2 Minutes
        
        Keyword arguments:
        :param: bot -- discord.Client | discord.ext.commands.Bot | infinipy.core.Bot
        :param: api_key -- str
        :param: interval -- int | amount of time a post takes
        
        .. :warn: INTERVAL MUST BE ATLEAST 120 OR ELSE YOU'LL BE RATELIMITED
        
        """

        assert interval >= 120, 'Interval must be atleast 120 Seconds due to ratelimiting Issues'

        self.key = api_key
        self.bot = bot
        self.session = SyncAPISession(self.key)
        self.t = threading.Thread(target=self.__start__)
        self.interval = interval    

    def start(self):
        self.t.start()

    def __start__(self):
        while True:
            self.session.postStats(self.bot)
            print("[+] A Post was made")
            time.sleep(self.interval)
    

class APISession:
    def __init__(self,id):
        self.id = id
        self.endpoint = endpoint_for(self.id)

    def fetch(self):
        if self.endpoint.startswith("/bots"):
            return fetch_bot_sync(self.id)
        return fetch_user_sync(self.id)

def endpoint_for(user_id):
    """Determines whether an ID belongs to the /user or to /bots endpoint
    """
    error = fetch_bot_sync(user_id)
    if isinstance(error,RequestFailed):
            return f'/user/{user_id}'
    return f'/bots/{user_id}'

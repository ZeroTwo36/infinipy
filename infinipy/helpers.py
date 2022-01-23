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
        :param: bot -- discord.Client | discord.ext.commands.Bot
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
            if hasattr(self.bot,'shard_count'):
                shards = self.bot.shard_count
            else:
                shards = 0
            self.session.postStats(shards,len(self.bot.guilds))
            print("[+] A Post was made")
            time.sleep(self.interval)
    

class APISession:
    def __init__(self,id):
        self.id = id
        self.endpoint = endpoint_for(self.id)

    def fetch(self):
        if self.endpoint.startswith("/bots"):
            return fetchBotSync(self.id)
        return fetchUserSync(self.id)

def endpoint_for(user_id):
    """Determines whether an ID belongs to the /user or to /bots endpoint
    """
    req = requests.get(f"https://japi.rest/discord/v1/user/{user_id}").json()
    if "bot" in req and req["bot"] == True:
            return f'/bots/{user_id}'
    return f'/user/{user_id}'

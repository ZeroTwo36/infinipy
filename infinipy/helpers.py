import imp
from .core import *
import time
import threading
from .errors import BaseError, PrecaughtHttpStatusError, TooManyRequests


class AutoStatsUpdater:
    def __init__(self,bot,api_key, interval:int=120) -> None:
        """Automatically pushes a discord.py bot's stats to the API.

        Difference to Sync/AsyncAPISession? This Class automatically updates stats every
        2 Minutes
        
        Keyword arguments:
        :param: bot -- discord.Client | discord.ext.commands.Bot
        :param: api_key -- str
        :param: interval -- int | amount of time a post takes
        
        .. :warn: If Interval is LESS than 120, you're gonna run into a Ratelimit :|
        
        """

        if(interval < 120):
            raise PrecaughtHttpStatusError(f'''
        W                             
       WWW          
       WWW          
      WWWWW         
W     WWWWW     W   
WWW   WWWWW   WWW   
 WWW  WWWWW  WWW    
  WWW  WWW  WWW     
   WWW WWW WWW      
     WWWWWWW        
  WWWW  |  WWWW     
        |           
        |
    HTTP Error 420
  Enhance your calm
Thou shalt not be RateLimited.
Please set the interval to 120 or more
            ''')


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
    
def endpoint_for(user_id):
    """Determines whether an ID belongs to the /user or to /bots endpoint
    """
    req = requests.get(f"https://japi.rest/discord/v1/user/{user_id}").json()
    if "bot" in req["data"] and req["data"]["bot"] == True:
        return f'/bots/{user_id}'
    return f'/user/{user_id}'

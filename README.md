# Infini.Py

## Installation:
**Via PIP**:

  pip install git+https://github.com/ZeroTwo36/infinipy
  

## Get started:
```py
import infinipy

USER_ID = 899722893603274793
BOT_ID  = 909882795768315986
user = infinipy.fetchUserSync(USER_ID) # Will return infinipy.core.User()
bot = infinipy.fetchBotSync(BOT_ID) # Will return infinipy.core.Bot()
```

## Examples:
```py
print("Bot Stats:")
print("Votes: "+str(bot.analytica['votes'])
print("User Stats:")
print("Nick: " + user.name + "\nBio: "+ user.about) 
```

## Sessions

A Session is initialized once and can - as long as it's not nullified - Post Stats, Get Stats

```py
from infinipy.helpers import APISession, endpoint_for

session = APISession("BOT_ID")
obj = session.fetch()
```
In a Bot maybe like this:
```py
@client.command()
async def iblinfo(ctx,_Id):
  session = APISession("Auth Key", _Id)
  object = session.fetch()
  await ctx.send(object.name)
```


## Update Bot Stats

To Work with everyday Python, Use the :class: `SyncAPISession`

In theory, usage would look like this:
```py
from infinipy import SyncAPISession

api = SyncAPISession("api_key", bot_id)
api.postStats(shard_count, server_count, user_count)
```  

While in a script, it could look something like this:
```py
from infinipy import SyncAPISession
from dotenv import load_dotenv
import os
from discordbot import botclient

load_dotenv()

api = SyncAPISession(os.environ.get("ibl_api_key"), bot_id)
api.postStats(bot.shards,len(bot.guilds), len(list(bot.get_all_users())))
```

Async is the same, but postStats must be *await*ed.   
This is recommended to post real-time stats, like this:  
```py
from infinipy import AsyncAPISession
from dotenv import load_dotenv
import os
load_dotenv()

@bot.event
async def on_guild_join(guild):
  api = AsyncAPISession(os.environ.get("ibl_api_key"), bot_id)
  await api.postStats(bot.shards,len(bot.guilds), len(list(bot.get_all_users())))
```
Note, that on both Classes you can get the API's response like this:  
```py
response = api.session["UPDATE_RESPONSE"]
print(response)
```

## Adding an AutoPoster because I'm bored
AutoPosters update the Bot's statistics every so and so seconds, kinda like this:  

```py
from infinipy.helpers import AutoStatsUpdater
from mycoolbot import bot # Your Bot instance

interval = 120 # Must be >= 120

poster = AutoStatsUpdater(bot,"API_KEY_HERE",interval)
poster.start()
```


## Webhooks

```py
from infinipy.webhooks import Webhook

wh = Webhook(bot,"SECRET_KEY",port=1234)
wh()
```

## Yay, another Update!
I finally decided to add compatibility (At least a bit) for Infinity's API v5

Hope to see you soon!  
~ ZeroTwo36

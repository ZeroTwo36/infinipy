# infinipy

## Okay, hear me out:
I know about IBLPy. I made this Library out of boredom, pretty much.

PLUS: InfiniPy has some neat features - like the endpoint_for function.

### Get started:
```py
import infinipy

USER_ID = 899722893603274793
BOT_ID  = 909882795768315986
user = infinipy.fetchUserSync(USER_ID) # Will return infinipy.core.User()
bot = infinipy.fetchBotSync(BOT_ID) # Will return infinipy.core.Bot()
```

### Examples:
```py
print("Bot Stats:")
print("Votes: "+str(bot.analytica['votes'])
print("User Stats:")
print("Nick: " + user.name + "\nBio: "+ user.about) 
```
### Determining if Someone's a User or a bot using endpoint_for()

Ah yes, the Problem of determining if someone's a Bot or not...  
So, let's assume that you want to make a bot that can get Infos using an info command  
**BUT** it must be able to detect wether you specified a User or a Bot.  

Well, the infinipy.helpers module added in V0.2 should be able to help you!

In theory, this is the code:
```py
from infinipy.helpers import APISession, endpoint_for

session = APISession("BOT_ID")
obj = session.fetch()
```
In a Bot maybe like this:
```py
@client.command()
async def iblinfo(ctx,_Id):
  session = APISession(_Id)
  object = session.fetch()
  await ctx.send(object.name)
```

And that's it for V0.2!

## Update Bot Stats
Okay, you want everybody to see how cool your Bot is. That's great!  
In V0.3, I have added APISessions to do exactly that!  

Whether you're using a script to just post stats there, or want to real-time update your Bot's Statistics on IBL, I gotcha!  

For simple Scripts, I recommend to use the **SyncAPISession Class**:

In theory, usage would look like this:
```py
from infinipy import SyncAPISession

api = SyncAPISession("api_key")
api.postStats(shard_count, server_count)
```  

While in a script, it could look something like this:
```py
from infinipy import SyncAPISession
from dotenv import load_dotenv
import os
from discordbot import botclient

load_dotenv()

api = SyncAPISession(os.environ.get("ibl_api_key"))
api.postStats(bot.shards,len(bot.guilds))
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
  api = AsyncAPISession(os.environ.get("ibl_api_key"))
  await api.postStats(bot.shards,len(bot.guilds))
```
Note, that on both Classes you can get the API's response like this:  
```py
response = api.session["UPDATE_RESPONSE"]
print(response)
```

### Adding an AutoPoster because I'm bored
AutoPosters update the Bot's statistics every so and so seconds, kinda like this:  

```py
from infinipy.helpers import AutoStatsUpdater
from mycoolbot import bot # Your Bot instance

interval = 120 # Must be >= 120

poster = AutoStatsUpdater(bot,"API_KEY_HERE",interval)
poster.start()
```

### Adding WebHooks and hoping it works
Hey! It's been a while, but I'm back with new, exciting Features for V0.3! **Webhooks!**  
Basically, a Webhook is triggered whenever a Vote is fired. Then a POST-Request to the Webhook will be made  

I used FLASK for the WebHooks. You implement them like so:

```py
from infinipy.webhooks import webhook
from infinipy import fetchBotSync

bot = fetchBotSync(909882795768315986)

@webhook(ibl=bot,secret="supersecret",route="/onvote")
def on_vote(request,hook):
  print("Vote fired!")
  
on_vote.listen()
```

Or:

```py
from infinipy import fetchBotSync

bot = fetchBotSync(909882795768315986)
@bot.webhook(secret="supersecret",route="/onvote")
def on_vote(request,hook):
  print("Vote fired!")
  
on_vote.listen()
```

This will print "Vote fired!" on your screen whenever a Vote is fired.

*This Feature took me insanely long to make. I hope you like it*

Hope to see you soon!  
~ ZeroTwo36

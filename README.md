# infinipy

## Okay, hear me out:
I know about ibl.py. I made this Library out of boredom, pretty much.

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
print("Votes: "+str(bot.analytica['votes']
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

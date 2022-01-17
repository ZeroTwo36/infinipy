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

## Just a small notice
Imagine this scenario for a minute...:

> I make a Library  
> Someone Tells me, how much it sucks  
> They clone it and send their Code to me saying they "fixed" it  
> After taking a look, the only change I notice is that they changed the function's docstrings  
> They release it anyways to a server  
> people believe them and credit them even though they just stole my code.  
If someone did that, Developers would tear them apart, eh?   

Nobody would actually allow them to get away with this, correct? 

*Correct?*

***Correct?***

...well...

It's already happened twice since the initial release that people took my code and reuploaded it with 0 Changes (Maybe modified a docstring)  
*And people accept it.* They don't tear the Guy, whose name I will respectfully not reveal here, apart, they chose to attack me and how much my code sucks

Listen. **I know my code sucks.** That doesn't mean that if someone clones it, it's suddenly better.  
You *can* create pull requests and improve my code. I would actually be happy about that.  
What I am *not* happy with, is people taking my Code and claiming it to be theirs.  

If you've read up until here, Thanks. I will propably move this part to a seperate gist later on.

~ ZeroTwo36

from .errors import RequestFailed, InfinipyBaseException
import aiohttp
import requests

class User:
    def __init__(self,id,nickname:str,about:str,certified_dev:bool,developer:bool,staff:bool,links):
        self.id = id
        self.name = nickname
        self.about = about
        self.certified = certified_dev
        self.dev_status = developer
        self.staff_status = staff
        self.website = links.get('website')
        self.github = links.get('github')

class Bot:
    def __init__(self,id,name,tags,prefix,owner,additional_owners,short,long,library,nsfw,programs,analytics,links,**other):
        self.id = id
        self.name = name
        self.tags = tags.split(",")
        self.prefix = prefix
        self.owner = owner
        self.additional_owners = additional_owners
        self.short = short
        self.long = long
        self.lib = library
        self.nsfw = not not nsfw
        self.programs = programs
        self.analytica = analytics
        self.links = links
        self.other = other

async def fetch_bot(id):
    async with aiohttp.ClientSession() as cs:
        resp = await cs.get(f"https://api.infinitybotlist.com/bots/{id}")

    if resp.status>=400 :
        return RequestFailed(await resp.json())
    resp.raise_for_status()
    json = await resp.json()

    return Bot(id,**json)
    
def fetch_bot_sync(id):
    resp = requests.get(f"https://api.infinitybotlist.com/bots/{id}")


    if resp.status_code>=400 :
        return RequestFailed(resp.json())
    resp.raise_for_status()
    json = resp.json()

    return Bot(id,**json)


async def fetch_user(id):
    async with aiohttp.ClientSession() as cs:
        resp = await cs.get(f"https://api.infinitybotlist.com/user/{id}")

    if resp.status>=400 :
        return RequestFailed(await resp.json())
    resp.raise_for_status()
    json = await resp.json()

    return User(id,**json)

def fetch_user_sync(id):
    resp = requests.get(f"https://api.infinitybotlist.com/user/{id}")

    if resp.status_code>=400 :
        return RequestFailed(resp.json())

    resp.raise_for_status()
    json = resp.json()

    return User(id,**json)

async def has_voted(user,bot_for):
    
    async with aiohttp.ClientSession() as cs:
        resp = await cs.get(f"https://api.infinitybotlist.com/votes/{bot_for}/{user}")

    resp.raise_for_status()
    json = await resp.json()
    return not not json['hasVoted']

def has_voted_sync(user,bot_for):
    resp = requests.get(f"https://api.infinitybotlist.com/votes/{bot_for}/{user}")

    resp.raise_for_status()
    json = resp.json()
    return not not json['hasVoted']

def endpoint_for(user_id):
    """Determines whether an ID belongs to the /user or to /bots endpoint
    """
    error = fetch_bot_sync(user_id)
    if isinstance(error,RequestFailed):
            return f'/user/{user_id}'
    return f'/bots/{user_id}'
    


class APISession:
    def __init__(self,id):
        self.id = id
        self.endpoint = endpoint_for(self.id)

    def fetch(self):
        if self.endpoint.startswith("/bots"):
            return fetch_bot_sync(self.id)
        return fetch_user_sync(self.id)


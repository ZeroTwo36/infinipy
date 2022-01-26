import json
from .errors import RequestFailed, InfinipyBaseException
import aiohttp
import requests
from .constants import *
import typing as t

class Session:
    def __init__(self):
        self = {}

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

    @property
    def stats(this):
        return vars(this)

    def hasUserVoted(self,user):
        resp = requests.get(f"https://api.infinitybotlist.com/votes/{self.id}/{user}")

        resp.raise_for_status()
        json = resp.json()
        return not not json['hasVoted']



        
class AsyncAPISession:
    def __init__(self,api_token):
        self.token = api_token
        self.session = Session()

    async def _post(self,endpoint,authorize,predef_headers,jsondata):
        async with aiohttp.ClientSession() as cs:
            if not predef_headers:
                headers = {
                    'User-Agent':f'Infpy/{__version_info__}'
                }
                if not not authorize:
                    headers['authorization'] = self.token
            else:
                headers = predef_headers
            resp = await cs.post(f'https://api.infinitybotlist.com/{endpoint}',headers=headers,json=jsondata)
            resp.raise_for_status()
            return await resp.json()

    async def postStats(self,shards:int=0,servers:int=0):
        data = {
            'servers':servers,
            'shards':shards
        }
        resp = await self._post('bots/stats',jsondata=data)
        self.session['UPDATE_RESPONSE'] = resp

class SyncAPISession:
    def __init__(self,api_token):
        self.token = api_token
        self.session = Session()

    def _post(self,endpoint,authorize:bool=True,predef_headers:dict=None,jsondata:dict={}):
        
            if not predef_headers:
                headers = {
                    'User-Agent':f'Infpy/{__version_info__}',
                    "Content-Type": "application/json"
                }
                if not not authorize:
                    headers['Authorization'] = self.token
            else:
                headers = predef_headers
            print(headers)
            resp = requests.post(f'https://api.infinitybotlist.com/{endpoint}',headers=headers,json=jsondata)
            resp.raise_for_status()
            return resp.json()

    def postStats(self,shards:int=0,servers:int=0):
        data = {
            'servers':servers,
            'shards':shards
        }
        resp = self._post('bots/stats',jsondata=data)
        self.session['UPDATE_RESPONSE'] = resp



def _requestHandle(endpoint):
    return json.loads(requests.get(f'https://api.infinitybotlist.com{endpoint}').text)
    
async def fetchBot(id):
    async with aiohttp.ClientSession() as cs:
        resp = await cs.get(f"https://api.infinitybotlist.com/bots/{id}")

    if resp.status>=400 :
        return None
    resp.raise_for_status()
    json = await resp.json()

    return Bot(id,**json)
    
def fetchBotSync(id):
    resp = requests.get(f"https://api.infinitybotlist.com/bots/{id}")


    if resp.status_code>=400 :
        return None
    resp.raise_for_status()
    json = resp.json()

    return Bot(id,**json)


async def fetchUser(id):
    async with aiohttp.ClientSession() as cs:
        resp = await cs.get(f"https://api.infinitybotlist.com/user/{id}")

    if resp.status>=400 :
        return RequestFailed(await resp.json())
    resp.raise_for_status()
    json = await resp.json()

    return User(id,**json)

def fetchUserSync(id):
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


    

import json as json
from .errors import RequestFailed, InfinipyBaseException
import aiohttp
import requests
from .constants import __version_info__
import typing as t
import multidict
from .webhooks import WebHook

class Session(multidict.CIMultiDict):
    def __init__(self,**kwds):
        super().__init__(kwds)

class BaseUser:
    def __init__(self,id,links,name,**kwargs):
        self.id = id
        self.name = name
        self.links = links
        self.website = links.get('website')
        self.github = links.get('github')
        for k in list(kwargs.keys()):
            self.__setattr__(k,kwargs.get(k))

class User(BaseUser):
    def __init__(self,id,nickname:str,about:str,certified_dev:bool,developer:bool,staff:bool,links):
        super().__init__(id,links,nickname,about=about,certified_dev=certified_dev,developer=developer,staff=staff)
    
    @property
    def jsonify(this):
        return vars(this)

    def hasVotedFor(self,bot):
        resp = requests.get(f"https://api.infinitybotlist.com/votes/{bot}/{self.id}")

        resp.raise_for_status()
        json = resp.json()
        return not not json['hasVoted']


class Bot(BaseUser):
    def __init__(self,id,name,tags,prefix,owner,additional_owners,short,long,library,nsfw,programs,analytics,links,**other):
        super().__init__(id,links,name,prefix=prefix,owner=owner,additional_owners=additional_owners,short=short,long=long,library=library,nsfw=nsfw,programs=programs,tags=tags.split(","),analytica=analytics,**other)

    @property
    def jsonify(this):
        """
        Returns the Classes Variables as JSON/Dicts
        """
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
        """
        Non-async API Session

        :param api_token: An API Token for a Bot
        """
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
        """
        Post stats to IBL's API

        :param shards: Shard Count
        :param servers: Server Count 

        Sample Usage:
        
        .. code-block:: py
            from infinipy import SyncAPISession

            cs = SyncAPISession("API_TOKEN")
            cs.postStats(servers=12)
        """
            
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


    

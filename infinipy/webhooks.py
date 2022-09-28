from infinipy import syncHookHTTP, hookHTTP
import asyncio

class SyncWebHook(object):
    def __init__(self,ibl_client,secret_key,port=3848,func=None):
        self.ibl_client =ibl_client
        self.secret_key = secret_key
        self.port = port
        self.func = func
        SyncHookHTTP.func = self.func
        SyncHookHTTP.wh = self


    def create_app(self):
        SyncHookHTTP.router.run("0.0.0.0", self.port)

    def __call__(self, *args, **kwds):
        self.create_app()

class WebHook(object):
    def __init__(self,ibl_client,secret_key,port=3848,func=None):
        self.ibl_client =ibl_client
        self.secret_key = secret_key
        self.port = port
        self.func = func
        hookHTTP.func = self.func
        hookHTTP.wh = self


    async def _create_app(self):
        hookHTTP.router.run("0.0.0.0", self.port)

        
    def startAsLoop(self):
        """Run a main Coroutine. Don't use inside a bot directly, as it's Blocking. 
        Use `~.start()` instead
        """
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._create_app())
        return True
    
    def __call__(self):
        asyncio.run(self._create_app())
    
    def start(self):
        asyncio.run(self._create_app())

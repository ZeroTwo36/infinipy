from .core import *

class APISession:
    def __init__(self,id):
        self.id = id
        self.endpoint = endpoint_for(self.id)

    def fetch(self):
        if self.endpoint.startswith("/bots"):
            return fetch_bot_sync(self.id)
        return fetch_user_sync(self.id)

def endpoint_for(user_id):
    """Determines whether an ID belongs to the /user or to /bots endpoint
    """
    error = fetch_bot_sync(user_id)
    if isinstance(error,RequestFailed):
            return f'/user/{user_id}'
    return f'/bots/{user_id}'
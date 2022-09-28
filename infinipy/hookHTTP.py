import json
from quart import Quart, request
import typing as t
import asyncio

router = Quart(__name__)


async def check(webhook,func,request):
    """
    The check function is used to verify that the request is coming from a trusted source.
    The check function takes in a webhook object and returns a decorator which will run the decorated function only if
    the request is authenticated with the correct secret key.
    
    :param webhook: Used to Pass the webhook object to the predicate function.
    :return: A function that is used as a decorator.    
    """
    def predicate(*args, **kwargs):
        if request.method == "POST" and request.headers.get("Authorization") == webhook.secret_key:
            return func(*args, **kwargs)
        return None
    
    return predicate()

@router.route("/", methods=['GET','POST'])
async def index():
    res = await check(wh,func,request)
    return json.dumps({"success": True if res else False})

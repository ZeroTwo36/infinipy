import json
from flask import Flask, request
import typing as t


current_request = request
router = Flask(__name__)


def check(webhook,func,request):
    """
    The check function is used to verify that the request is coming from a trusted source.
    The check function takes in a webhook object and returns a decorator which will run the decorated function only if
    the request is authenticated with the correct secret key.
    
    :param webhook: Used to Pass the webhook object to the predicate function.
    :return: A function that is used as a decorator.    
    """
    
    if request.method == "POST" and request.headers.get("Authorization") == webhook.secret_key:
        func()
        return True
    return False

@router.route("/", methods=['GET','POST'])
def index():
    res = check(wh,func,request)
    return json.dumps({"success": True if res else False})

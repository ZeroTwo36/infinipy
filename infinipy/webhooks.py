from flask import Flask, request
import requests
import json
from .errors import WebhookFailure
from threading import Thread
from flask_cors import CORS

class WebHook(object):
    flask = Flask('')
    route = "/hook"
    def __init__(self,iblclient,secret,handler,host,port,route="/hook",enable_cors=False):
        self.ibl = iblclient
        self.secret = secret
        self.handler = handler
        self.host = host
        self.port = port
        self.route = route
        self.flask = Flask('')
        if enable_cors:
            CORS(self.flask)

    @flask.route(route,methods=['GET', 'POST'])
    def _handle(self):
        """
        The _handle function is the actual function that will be called when your endpoint is invoked. 
        It must have a single argument which will be a dict containing the arguments to your function.
        
        :param self: Used to access variables that belongs to the class.
        :return: the value of the _value attribute.
        """
        if request.headers.get('Authorization') == self.secret:    
            return self.handler(request, self)
        
        error = WebhookFailure(400,"Webhook Secret doesn't Match")
        print(error)
        return json.dumps({"error":str(error),"fatal":True})

    def listen(self):
        """
        The listen function listens for messages from the client.
        It is called when a new connection is made to the server.
        
        :param self: Used to refer to the object itself.
        :return: the value of the listen function.
        """
        
        t = Thread(target=self._run)
        t.start()


    def _run(self):
        self.flask.run(self.host,self.port)

def webhook(**args):
    """
    The webhook function is a decorator that registers a function as an endpoint for webhooks.
    The decorated function will be called when the specified IBL instance receives a webhook request with the specified secret.
    
    :param **args: Used to pass in the parameters that are used to configure the webhook.
    :return: a decorator that can be used to register a function for the webhook.
    """
    
    def predicate(func):
        return WebHook(args.get("ibl"),args.get("secret"),func,args.get("host","0.0.0.0"),args.get("port",2184),args.get("route","/hook"))

    return predicate


from infinipy import hookHTTP


class WebHook(object):
    def __init__(self,ibl_client,secret_key,port=3848,func=None):
        self.ibl_client =ibl_client
        self.secret_key = secret_key
        self.port = port
        self.func = func
        hookHTTP.func = self.func
        hookHTTP.wh = self


    def create_app(self):
        hookHTTP.router.run("0.0.0.0", self.port)

    def __call__(self, *, require_cors=False):
        self.create_app()

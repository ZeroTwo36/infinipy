from requests import HTTPError


class InfinipyBaseException(Exception):
    """Something has failed"""


class RequestFailed(HTTPError):
    """Request failed (Status Code>=400)"""
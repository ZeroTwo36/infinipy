from requests import HTTPError


class InfinipyBaseException(Exception):
    """Something has failed"""


class RequestFailed(HTTPError):
    """Request failed (Status Code>=400)"""

class BaseError:
    def __init__(self,status_code,name,details):
        self.status = status_code
        self.name = name
        self.details = details

    def __str__(self) -> str:
        return f'Error; {self.name} (HTTPError {self.status}): {self.details}'

class TooManyRequests(BaseError):
    def __init__(self,details):
        super().__init__(420,'Enhance your Calm!',details)

class PrecaughtHttpStatusError(InfinipyBaseException):
    """Run a .check() for every HTTP Request to check if it's even possible"""

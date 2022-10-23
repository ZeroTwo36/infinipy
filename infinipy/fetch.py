import requests, aiohttp

def fetch(url, headers={}, body={}, files={}, method="GET"):
    return requests.request(method, url, headers=headers, json=body, files=files)


async def aiofetch(url, headers={}, body={}, files={}, method="GET"):
    return  await aiohttp.request(method, url, headers=headers, json=body, files=files)

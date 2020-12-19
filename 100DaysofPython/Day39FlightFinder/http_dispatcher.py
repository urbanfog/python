import requests


class HTTPDispatcher:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, url: str) -> None:
        self.url = url
        self.header = {}

    def get(self, params="", end_point="") -> dict:
        get = requests.get(url=self.url+end_point,
                           params=params, headers=self.header)
        get.raise_for_status()
        print("Sent")
        return get.json()

    def post(self, params, end_point=""):
        post = requests.post(url=self.url+end_point,
                             json=params, headers=self.header)
        post.raise_for_status()
        print("Created")
        print(post.request.data)
        print(post.text)

    def put(self, header, params, end_point=""):
        put = requests.put(url=self.url+end_point, json=params, headers=header)
        put.raise_for_status()
        print("Updated")
        print(put.request.url)
        print(put.text)

    def delete(self, header, end_point=""):
        delete = requests.delete(url=self.url+end_point, headers=header)
        delete.raise_for_status()
        print("Deleted")
        print(delete.request.url)
        print(delete.text)

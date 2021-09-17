import requests
from typing import Tuple, Union


class ZenSerp:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.session()

        self.status_link = 'https://app.zenserp.com/api/v2/status'
        self.trends_link = 'https://app.zenserp.com/api/v1/trends'

    def get_trends(self, params: Tuple[Tuple[str, str], ...], json: bool = True) -> Union[dict, requests.Response]:
        response = self.session.get(self.trends_link, params=params, headers={'apikey': self.api_key})
        response = self.__generic_check(response)
        if json:
            return response.json()
        return response

    def get_status(self) -> dict:
        response = self.session.get(self.status_link, headers={'apikey': self.api_key})
        return self.__generic_check(response).json()

    def __generic_check(self, response: requests.Response) -> requests.Response:
        if response.ok:
            return response
        if self.get_status()['remaining requests'] <= 0:
            raise requests.ConnectionError('Api key is out of requests')
        raise requests.ConnectionError('Could not connect to host servers')


if __name__ == '__main__':
    myKey = ''
    serp = ZenSerp(myKey)
    print(serp.get_trends(params=(("keyword[]", "Joe Biden"), ("keyword[]", "Donald Trump"))))
    print(serp.get_status())

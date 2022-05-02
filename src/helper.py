import requests


class BaseApi:

    def __init__(self):
        self._base_url: str | None = None
        self._base_header: dict | None = None

    def _get(self, endpoint: str, headers: dict = None) -> requests.Response:
        if self._base_header and headers:
            headers.update(self._base_header)
        return requests.get(url=f'{self._base_url}{endpoint}',
                            headers=headers)

    def _post(self, endpoint: str, body: dict = None, headers: dict = None) -> requests.Response:
        if self._base_header and headers:
            headers.update(self._base_header)
        return requests.post(url=f'{self._base_url}{endpoint}', data=body,
                             headers=headers)

    def _put(self, endpoint: str, body: dict = None, headers: dict = None) -> requests.Response:
        if self._base_header and headers:
            headers.update(self._base_header)
        return requests.put(url=f'{self._base_url}{endpoint}', data=body,
                            headers=headers)

    def _delete(self, endpoint: str, headers: dict = None) -> requests.Response:
        if self._base_header and headers:
            headers.update(self._base_header)
        return requests.put(url=f'{self._base_url}{endpoint}',
                            headers=headers)

    def _patch(self, endpoint: str, body: dict = None, headers: dict = None) -> requests.Response:
        if self._base_header and headers:
            headers.update(self._base_header)
        return requests.put(url=f'{self._base_url}{endpoint}', data=body,
                            headers=headers)

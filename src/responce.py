import logging
from datetime import datetime
import allure
from curlify import to_curl
from requests import Response


class AssertableResponse:

    def __init__(self, response: Response):
        self._curl: str = to_curl(response.request)
        allure.attach(f'request url={response.request.url} body={response.request.body}'
                      f'\nresponse status code={response.status_code} body={response.text}'
                      f'\n{self._curl}',
                      f'request_{datetime.today().strftime("%d-%m_%H:%M")}',
                      allure.attachment_type.TEXT)
        logging.info(f'request url={response.request.url} body={response.request.body}')
        logging.info(f'response status code={response.status_code} body={response.text}')
        logging.info(f'{self._curl}')
        self._response = response

    @allure.step('Check that {1}')
    def should_have(self, condition):
        logging.info(f'check that {str(condition)}')
        condition.match(self._response)
        return self

    def body(self) -> dict | list:
        return self._response.json()

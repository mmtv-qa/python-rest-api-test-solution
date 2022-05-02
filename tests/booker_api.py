from allure import step

from src.helper import BaseApi
from src.responce import AssertableResponse


class BookerApi(BaseApi):

    def __init__(self):
        super().__init__()
        self._base_url = 'https://restful-booker.herokuapp.com'  # os.getenv('BOOKER_API')
        self._base_headers = {'content-type': 'application/json'}
        self._valid_creds = {'username': 'admin',  # os.getenv('BOOKER_API_USERNAME')
                             'password': 'password123'}  # os.getenv('BOOKER_API_PASSWORD')
        self._token = self.auth(body=self._valid_creds).json()

    def auth(self, body: dict):
        return self._post(endpoint='/auth', body=body)

    @step('Authentication with valid creds')
    def authorization_with_valid_creds(self):
        return AssertableResponse(self.auth(body=self._valid_creds))

    @step('Authentication with creds: username={1} password={2}')
    def authorization_with_invalid_creds(self, username: str, password: str):
        creds = {'username': username, 'password': password}
        return AssertableResponse(self.auth(body=creds))

    @step('Get all booking ids')
    def get_booking_ids(self):
        return AssertableResponse(self._get(endpoint='/booking', headers=self._token))

    @step('Get booking by id={1}')
    def get_booking_by_id(self, booking_id: int):
        return AssertableResponse(self._get(endpoint=f'/booking/{str(booking_id)}/', headers=self._token))

    @step('Create booking')
    def create_booking(self, data):
        return AssertableResponse(self._post(endpoint='/booking', body=data))

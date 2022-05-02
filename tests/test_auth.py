import hamcrest
from allure import title
from pytest import mark

from tests.booker_api import BookerApi
from src.conditions import status_code, body, schema
from tests.schemas import Schema


@mark.smoke
@title('Test authorization with valid credentials')
def test_authorization_with_valid_credentials():
    response = BookerApi().authorization_with_valid_creds()
    response.should_have(status_code(200))
    response.should_have(schema(Schema.AuthToken))


@title('Test authorization with invalid credentials')
def test_authorization_with_invalid_credentials(faker):
    BookerApi() \
        .authorization_with_invalid_creds(faker.name(), faker.password()) \
        .should_have(body('$.reason', hamcrest.equal_to('Bad credentials')))

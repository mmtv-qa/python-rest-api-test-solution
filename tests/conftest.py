from faker import Faker
from pytest import fixture


@fixture(scope='session')
def faker():
    faker = Faker()
    return faker

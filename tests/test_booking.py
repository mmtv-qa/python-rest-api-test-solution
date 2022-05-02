from random import choice, randint

import hamcrest
from allure import title
from tests.schemas import Schema
from src.conditions import status_code, schema, body
from tests.booker_api import BookerApi


@title('Test get booking object by ID')
def test_get_booking_by_id():
    booking_id: int = 1
    response = BookerApi().get_booking_by_id(booking_id)
    response\
        .should_have(status_code(200))\
        .should_have(schema(Schema.Booking))


@title('Test add new booking')
def test_create_booking(faker):
    data = {"firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": randint(100, 150),
            "depositpaid": choice((True, False)),
            "bookingdates": {
                "checkin": faker.date(),
                "checkout": faker.date()
            },
            "additionalneeds": "Breakfast"
            }
    response = BookerApi().create_booking(data=data)
    response \
        .should_have(status_code(200)) \
        .should_have(schema(Schema.Booking))


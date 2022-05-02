from dataclasses import dataclass


@dataclass
class Schema:
    Booking = {
        "firstname": {
            "type": "string",
            "empty": False
        },
        "lastname": {
            "type": "string",
            "empty": False
        },
        "totalprice": {
            "type": "number",
            "empty": False
        },
        "depositpaid": {
            "type": "boolean",
            "empty": False
        },
        "bookingdates": {'type': 'dict',
                         "schema": {"checkin": {
                             "type": "datetime",
                             "empty": False
                         },  "checkout": {
                             "type": "datetime",
                             "empty": False}}
                         },
        "additionalneeds": {
            "type": "string"
        }
    }

    AuthToken = {
        "token": {"type": "string", "empty": False}
    }

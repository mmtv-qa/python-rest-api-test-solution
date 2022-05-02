import abc
import os.path
from json import load
from os.path import expanduser, abspath
from pprint import pprint

import jsonpath_rw
from cerberus import Validator
from hamcrest import assert_that
from requests import Response


class Condition:

    @abc.abstractmethod
    def match(self, response: Response):
        return


class StatusCodeCondition(Condition):

    def __init__(self, code: int):
        self._status_code = code

    def match(self, response: Response):
        assert response.status_code == self._status_code, \
            f'status code don`t equal to {self._status_code}'

    def __repr__(self):
        return f'status code is {self._status_code}'


class BodyCondition(Condition):

    def __init__(self, json_path, matcher):
        self._json_path = json_path
        self._matcher = matcher

    def match(self, response: Response):
        json = response.json()
        content = jsonpath_rw.parse(self._json_path).find(json)[0].value
        assert_that(content, self._matcher)

    def __repr__(self):
        return f'body is {self._json_path} {self._matcher}'


class SchemaCondition(Condition):

    def __init__(self, json_schema: str):
        self._json_schema = json_schema
        self._validator = Validator(self._json_schema)

    def match(self, response: Response):
        json = response.json()
        assert self._validator(json), \
            f'{json}\ndon`t match\n{self._json_schema}'

    def __repr__(self):
        return f'jsonschema is {self._json_schema}'



status_code = StatusCodeCondition
body = BodyCondition
schema = SchemaCondition


if __name__ == '__main__':
    pprint(SchemaCondition.get_schema("booking"))
from functools import partial
from re import findall

from flask import request

from wtforms.validators import InputRequired, NumberRange
from wtforms import Form, StringField, IntegerField


RequiredString = partial(StringField, validators=[InputRequired()])


def integer_field(start=0, end=100):
    validators = [NumberRange(start, end)]
    return IntegerField(validators=validators)


class FForm(Form):
    def __init__(self):
        super().__init__(request.form)

    def validate(self):
        if request.method != "POST":
            return False
        return super().validate()


class WoWCheckItemForm(FForm):
    name = RequiredString("Item name")
    level = integer_field()


GET_NUMBERS = r"-?[0-9]+"


class PoEQualityCombination(FForm):
    values = RequiredString()

    @property
    def integers(self):
        return list(map(int, findall(GET_NUMBERS, self.values.data)))

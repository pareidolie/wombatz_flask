from functools import partial
from re import findall

from flask import request

from wtforms.validators import InputRequired, NumberRange, Regexp
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


TWENTY = "(20|1[0-9]|[0-9])"
VALIDATE_NUMBERS = r"^\s*{0}(\s*,?\s*{0})*\s*$".format(TWENTY)
GET_NUMBERS = r"[0-9]+"


class PoEQualityCombination(FForm):
    values = StringField(validators=[Regexp(VALIDATE_NUMBERS)])

    @property
    def integers(self):
        return list(map(int, findall(GET_NUMBERS, self.values.data)))


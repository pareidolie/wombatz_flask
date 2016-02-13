from json import dumps

from flask import Blueprint, Response, render_template

from ..menu import menu


COLORS = ["danger", "warning", "success", "info", "primary"]


def json(**kwargs):
    return dumps(dict(**kwargs))


def irange(start, end=None, step=1):
    if end is None:
        end = start
        start = 0
    yield from range(start, end + step, step)


main = Blueprint("main", "main")
menu.activate(main)

menu.push("Home")


@main.route("/")
@menu.add("Index", home=True)
def index():
    return render_template("main/index.html")


@main.route("/test/")
@menu.add("Test")
def test():
    return render_template("main/test.html")


@main.route("/stream/")
def stream():
    def generate():
        from time import sleep
        from random import choice

        for i in range(100):
            sleep(0.1)
            yield json(color=choice(COLORS))
        yield json(status="ok")

    return Response(generate(), mimetype="text/json")


menu.pop()

from .wow import wow
from .poe import poe

views = [main, wow, poe]

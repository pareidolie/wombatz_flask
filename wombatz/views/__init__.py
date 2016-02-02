from flask import Blueprint, render_template

from ..menu import menu


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
    return "Test"

menu.pop()

from .wow import wow
from .poe import poe

views = [main, wow, poe]

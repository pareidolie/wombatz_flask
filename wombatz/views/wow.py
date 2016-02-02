from flask import Blueprint, render_template

from ..forms import WoWCheckItemForm
from ..menu import menu


wow = Blueprint("wow", "wow", url_prefix="/wow/")
menu.activate(wow)


with menu.push("WoW"):
    @wow.route("/")
    @menu.add("Index")
    def index():
        return render_template("wow/index.html")

    @wow.route("check/", methods=["GET", "POST"])
    @menu.add("Item check")
    def check():
        form = WoWCheckItemForm()
        if form.validate():
            pass
        return render_template("wow/check.html", form=form)

from flask import Blueprint, flash, render_template

from ..forms import PoEQualityCombination
from ..function.poe import quality_combinations
from ..menu import menu


poe = Blueprint("poe", "poe", url_prefix="/poe/")
menu.activate(poe)


with menu.push("PoE"):
    @poe.route("/")
    @menu.add("Index")
    def index():
        return render_template("poe/index.html")

    @poe.route("quality/", methods=["GET", "POST"])
    @menu.add("Quality Check")
    def quality():
        form = PoEQualityCombination()
        result = None
        if form.validate():
            result = quality_combinations(form.integers)
            if result is None:
                flash("No combination reached a total of 40", "danger")
        return render_template("poe/quality.html", form=form, result=result)

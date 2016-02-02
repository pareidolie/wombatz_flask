from flask import Blueprint, flash, render_template

from ..forms import PoEQualityCombination
from ..function import has_larger_than, has_negative
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
            integers = form.integers
            if has_negative(integers):
                flash("Negative values don't make sense", "warning")
            if has_larger_than(20, integers):
                flash("Larger values than 20 don't make sense", "warning")
            result = quality_combinations(form.integers)
            if result is None:
                flash("No combination reached a total of 40", "danger")
            elif result[0] == 20:
                flash("Turn in a quality 20 item on its own", "warning")
        return render_template("poe/quality.html", form=form, result=result)

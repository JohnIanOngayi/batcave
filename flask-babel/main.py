#!/usr/bin/env python3

from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import date, datetime
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config["BABEL_DEFAULT_LOCALE"] = "es"
babel = Babel(app)


def get_locale():
    return "en"
    # return request.accept_languages.best_match(["en", "es", "de"])


@app.route("/", strict_slashes=False)
def index():

    car = gettext("car")
    us_num = numbers.format_decimal(1.2345, locale="en_US")
    se_num = numbers.format_decimal(1.2345, locale="sv_SE")
    de_num = numbers.format_decimal(1.2345, locale="de_DE")

    d = date(2000, 8, 8)

    us_date = dates.format_date(d, locale="en_US")
    se_date = dates.format_date(d, locale="sv_SE")
    # de_date = dates.format_date(d, locale="de_DE")
    de_date = format_date(d)

    dt = datetime(2000, 8, 8, 23, 8, 20, 99)

    us_datetime = dates.format_datetime(dt, locale="en_US")
    se_datetime = dates.format_datetime(dt, locale="sv_SE")
    de_datetime = dates.format_datetime(dt, locale="de_DE")

    results = {
        "us_num": us_num,
        "se_num": se_num,
        "de_num": de_num,
        "us_date": us_date,
        "se_date": se_date,
        "de_date": de_date,
        "us_datetime": us_datetime,
        "se_datetime": se_datetime,
        "de_datetime": de_datetime,
    }

    return render_template("index.html", results=results, car=car)


if __name__ == "__main__":
    app.run(debug=True)

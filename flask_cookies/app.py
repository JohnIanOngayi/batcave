#!/usr/bin/env python3

"""Module defines basic set_cookie, get_cookie"""

from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/new_cookie")
def new_cookie():
    resp = make_response("Hello  World")
    resp.set_cookie("myCookie", "myValue")
    return resp


@app.route("/show_cookie")
def show_cookie():
    cookie = request.cookies.get("myCookie")
    return cookie


if __name__ == "__main__":
    app.run(debug=True)

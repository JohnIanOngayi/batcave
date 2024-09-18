#!/usr/bin/env python3

"""
Module defines lil bit more advanced set_cookie, get_cookie
"""
from flask import Flask, app, request, make_response, render_template

app = Flask(__name__, template_folder="./templates")


@app.route("/")
def index():
    saved_name = request.cookies.get("saved_name")
    return render_template("index.html", saved_name=saved_name)


@app.route("/save_name", methods=["POST"])
def save_name():
    name = request.form.get("name")
    resp = make_response("We will now remember your name")
    if name:
        resp.set_cookie("saved_name", name)
    return resp


@app.route("/del_cookie")
def del_cookie():
    resp = make_response("Who you be?")
    resp.set_cookie("saved_name", "", expires=0)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

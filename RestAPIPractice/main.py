#!/usr/bin/env python3.8

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

    def post(self):
        return {"data": "Successful post request"}


api.add_resource(HelloWorld, "/helloworld")


if __name__ == "__main__":
    app.run(debug=True)

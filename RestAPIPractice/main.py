#!/usr/bin/env python3.8

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self, name="HelloWorld"):
        return {"data": name}

    def post(self, name="Successful post"):
        return {"data": f"Successful post {name}"}


api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)

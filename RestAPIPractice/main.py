#!/usr/bin/env python3.8

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


names = {
    "tim": {"name": "tim", "age": 26, "gender": "male"},
    "jane": {"name": "jane", "age": 23, "gender": "female"},
    "ian": {"name": "ian", "age": 24, "gender": "male"}
}


class HelloWorld(Resource):
    def get(self, name="HelloWorld"):
        return names[name]

    def post(self, name="Successful post"):
        return {"data": f"Successful post {name}"}


api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
#!/usr/bin/python3

import mongoengine
from datetime import datetime


class Snake(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.now)
    species = mongoengine.StringField(required=True)

    length = mongoengine.FloatField(required=True)
    name = mongoengine.StringField(required=True)
    is_venomous = mongoengine.BooleanField(required=True)

    meta = {"db_alias": "core", "collection": "snakes"}

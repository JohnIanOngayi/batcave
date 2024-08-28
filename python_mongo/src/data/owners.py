#!/usr/bin/env python3

import mongoengine
from datetime import datetime


class Owner(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True)

    snake_ids = mongoengine.ListField()
    cage_ids = mongoengine.ListField()

    meta = {"db_alias": "core", "collection": "owners"}

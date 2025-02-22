#!/usr/bin/python3

import mongoengine
from datetime import datetime
from data.bookings import Booking


class Cage(mongoengine.Document):
    register_date = mongoengine.DateTimeField(default=datetime.now)

    name = mongoengine.StringField(required=True)
    price = mongoengine.FloatField(required=True)
    sq_meters = mongoengine.FloatField(required=True)
    is_carpeted = mongoengine.BooleanField(required=True)
    has_toys = mongoengine.BooleanField(required=True)
    allow_dangerous_snakes = mongoengine.BooleanField(default=False)

    bookings = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {"db_alias": "core", "collection": "cages"}

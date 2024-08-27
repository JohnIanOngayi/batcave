#!/usr/bin/env python3

import mongoengine


def global_init():
    mongoengine.register_connection(alias="core", name="snake_bnb")

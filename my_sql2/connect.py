#!/usr/bin/python3

from sqlalchemy import create_engine, text

engine = create_engine(f"sqlite:///socialDB.db")

with engine.connect() as connection:
    test_result = connection.execute(text('select "Hello"'))
    print(test_result.all())

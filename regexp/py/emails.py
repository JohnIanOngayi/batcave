#!/usr/bin/python3
import re

emails = """
    JohnIanWOngayi@gmail.com
    johnian.ongayi@university.edu
    johnian-1234-ongayi@my-work.net
"""

pattern = re.compile(r"[A-Za-z0-9.-]+@[a-z-]+.[\w]+")
pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
matches = pattern.finditer(emails)
for match in matches:
    print(match)

#!/usr/bin/python3

import re

urls = """
https://www.google.com
https://greenholdings.com
https://youtube.com
https://www.nasa.com
"""

pattern = re.compile(r"https?://(www\.)?(\w+).(\w+)")
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3))

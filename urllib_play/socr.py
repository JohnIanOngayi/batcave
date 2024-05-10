#!/usr/bin/python3
from urllib import request, parse
resp = request.urlopen("https://www.wikipedia.org")
print (f"type: type(resp), {resp}")
print (resp.code)
print (resp.read().decode('utf-8'))

#!/usr/bin/env python3.8

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "helloworld/ian", {"mercs": 15})
print(response.json())

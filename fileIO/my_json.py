#!/usr/bin/python3

import json

with open('states.json', 'r') as json_file:
    json_data = json.load(json_file)
    for state in json_data['states']:
        print(state)

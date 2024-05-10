#!/usr/bin/python3

from urllib import request, parse

# x = request.urlopen('https://www.google.com')
# print(x.read())
url = 'https://pythonprogramming.net'
values = {'s': 'basic', 'submit': 'Search'}
data = parse.urlencode(values)
data = data.encode('utf-8')
req = request.Request(url, data)
response = request.urlopen(req)
print(response.read())

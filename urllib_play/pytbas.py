#!/usr/bin/python3

from urllib import request
page = request.urlopen('http://www.textfiles.com/etext/AUTHORS/POE/poe-raven-702.txt')
decoded_text = page.read().decode('utf-8')
page.close()
file = open('raven.txt', 'w')
file.write(decoded_text)
file.close()

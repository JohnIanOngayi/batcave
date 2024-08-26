#!/usr/bin/python3

import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )

johnian.com
coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match.span())
    print(text_to_search[match.span()[0]:match.span()[1]])

#!/usr/bin/python3

import re

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )

johnian.com
coreyms.com

cat
mat
pat
bat
2at

800-555-4321
900.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = "Start a sentence and then bring it to an end"
# d matches any digit
pattern = re.compile(r"\d{3}[.-]\d{3}[.-]\d{3}")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# with open("./py/data.txt", "r") as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

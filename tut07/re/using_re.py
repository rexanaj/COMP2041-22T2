#!/usr/bin/env python3

import re

email = 'z5555555@ad.unsw.edu.au'

# re.search
if re.search('@', email):
    print('Found the `@` symbol')
else:
    print("Didn't find the `@` symbol")

# Search at the start of the string
re.match('@', email)  # equivalent to -> re.search('^@', email)

# Search for a complete match
# equivalent to -> re.search('^z[0-9]{7}@ad.unsw.edu.au$', email)
re.fullmatch('z[0-9]{7}@ad.unsw.edu.au', email)

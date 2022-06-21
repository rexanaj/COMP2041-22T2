#!/bin/dash

mlalias cs2041.22T2.tut04 | 
sed -En '/Addresses/,/Owners/p' |
# grep -Ev ':'      # Quick way to extract only the zids based on regex
head -n -1 |        # Removes the last line 
tail -n +2 |        # Removes the first line
tr -d ' '

# sed -E 's/\s//g'  # Another way to remove whitespace

#!/bin/dash

mlalias cs2041.22T2.tut04 | 
sed -En '/Addresses/,/Owners/p' |
head -n -1 | # Removes the last line 
tail -n +2 | # Removes the first line
tr -d ' ' | 
while read zid; do 
    acc "$zid" | 
    grep -E '[A-Z]{4}[0-9]{4}t[0-3]_Student' | 
    sed -E 's/.*([A-Z]{4}[0-9]{4}).*/\1/g'
done | 
sort | 
uniq -c | 
sort -nr | 
sed -E 's/^\s+//g'

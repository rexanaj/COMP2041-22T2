#!/bin/bash 

cat "students.txt" | 
cut -d" " -f1 |  # extract the ids
sort | 
uniq -c |    # number of occurrences of zids
grep -Ev "^\s+1" | 
sed -E "s/^ +[0-9]+ //g"

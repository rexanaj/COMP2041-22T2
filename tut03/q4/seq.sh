#!/bin/sh

if [ $# -eq 1 ]; then 
    # LAST 
    FIRST=1 
    INCREMENT=1
    LAST=$1
elif [ $# -eq 2 ]; then 
    # FIRST LAST 
    FIRST=$1
    INCREMENT=1
    LAST=$2
elif [ $# -eq 3 ]; then 
    # FIRST INCREMENT LAST 
    FIRST=$1
    INCREMENT=$2
    LAST=$3
else 
    # Error 
    echo "Error: $0 expected 1-3 arguments"
    exit 1
fi 

# Error check for the case when INCREMENT is not a positive number
# [ "$INCREMENT" -eq "$INCREMENT" ] -> cheat way of checking for a number

# 2 >&1
# stderr -> stdout
if [ "$INCREMENT" -eq "$INCREMENT" ] 2> /dev/null && [ "$INCREMENT" -gt 0 ]; then 
    : # Placeholder for an empty if case 
else 
    echo "Error: $0 increment must be a positive number"
    exit 1
fi 

CURRENT="$FIRST"
while [ "$CURRENT" -le "$LAST" ]; do 
    # Main logic here
    # Print out current 
    echo "$CURRENT"

    # CURRENT = CURRENT + INCREMENT
    CURRENT=$(($CURRENT + $INCREMENT))
done 

# Success exit code 
exit 0

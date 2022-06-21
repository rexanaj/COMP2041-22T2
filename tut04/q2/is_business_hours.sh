#!/bin/dash 

# hour = "$(date "+%H")"
hour="$(date | cut -d' ' -f5 | cut -d':' -f1)"
echo "Hour is $hour"

if [ "$hour" -ge 9 ] && [ "$hour" -lt 17 ]; then 
    exit 0
else 
    exit 1
fi 

# Check the exit code using `echo $?`

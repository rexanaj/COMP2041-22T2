#!/bin/sh

for file in *.c
do 
    echo "$file includes:"
    grep -E "#include" $file | 
    sed -E 's/"$//g' | 
    sed -E 's/.*"/\t/g'

    # sed -E 's/#include "(.*)"/    \1/g'

    # Second approach
    # sed -E 's/"$//g' | 
    # sed -E 's/.*"/    /g'

    # First approach
    # grep -E "#include" $file | 
    # cut -d'"' -f2
done 


# Failure error code
# exit 1 

# Success error code 
exit 0

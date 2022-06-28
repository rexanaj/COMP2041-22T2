#!/bin/dash

# Set up the right environment for the tests 
# If `/.tigger` exists, then remove it 
if [ -d ".tigger" ]; then 
    rm -r ".tigger"
fi 

# Run 2041 tigger-init 
2041 tigger-init > /dev/null

# Run 2041 tigger-init again, but this time it should fail because .tigger
# exists already
output=$(2041 tigger-init 2> /dev/null)
status="$?"

# Testing error code
if [ "$status" -ne 1 ]; then 
    echo "$0: Test failed"
    exit 1
fi 

echo "$0: Test passed!"
exit 0

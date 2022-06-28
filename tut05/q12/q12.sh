#!/bin/dash

print_message() {
    if [ "$#" -eq 1 ]; then 
        # Just print the warning message 
        message="$1"
        echo "$0: Warning: $message"
    else 
        # Print error message and exit 
        status="$1"
        message="$2"
        echo "$0: Error: $message"
        exit "$1"
    fi 
}

echo "Test 1: A warning message"
print_message "This is a warning"

echo

echo "Test 2: An error message"
print_message 1 "This is an error"
# Check the status code

#!/bin/dash

# Shell function
top_and_bottom() {

    echo "$1 $2 $3"

    echo "================="
    # Print out the name of the file 
    echo "$1"

    echo "-----------------"

    # Print first and last line
    head -n 1 "$1"
    tail -n 1 "$1"

    echo
    echo "================="
}

# Loop through commandline arguments and run top_and_bottom on each file
for file in "$@"; do 
    top_and_bottom "$file" "hi" 1
done 

#!/bin/sh

if [ "$#" -ne 1 ]; then 
    echo "Usage: $0 dir_name"
    exit 1 
fi 

# test instead of [] 
if [ ! -d "$1" ]; then 
    echo "Error: $1 is not a directory"
    exit 1 
fi 

dir="$1"

# Loop through each file in the current directory 
cd "$dir"
for file in .* *; do 
    # -a 
    if [ "$file" != "." ] && [ "$file" != ".." ]; then 
        
        if [ -f "$file" ]; then 
            rm "$file"

        elif [ -d "$file" ]; then 
            echo "Delete $file?"
            read response 
            if [ "$response" = "yes" ]; then 
                rm -r "$file"
            fi 

        fi 

    fi 
done 

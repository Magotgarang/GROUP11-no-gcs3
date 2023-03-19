#!/bin/bash
#this shell script checks if there is a file called GCS_3_problems_20221105
file="GCS_3_problems_20221105"  
if [ ! -f "$file" ]; then         #if the file does not exist the script will return 2
    echo "2"
else
    if [ -s "$file" ]; then #if the file is not empty the script will then return 0
        echo "0"
    else
        echo "1" #if the file is empty then the script shall return zero
    fi
fi

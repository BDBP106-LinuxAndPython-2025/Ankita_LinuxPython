#!/bin/bash

# Function to find maximum of two numbers
function maximum {
    local num1=$1
    local num2=$2

    if [ "$num1" -gt "$num2" ]; then
        echo "Maximum is: $num1"
    else
        echo "Maximum is: $num2"
    fi
}



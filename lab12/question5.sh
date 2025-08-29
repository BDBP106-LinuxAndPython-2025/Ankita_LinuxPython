#!/bin/bash

# Function to divide two numbers
function divide {
    local num1=$1
    local num2=$2

# Check for division by zero
    if [ "$num2" -eq 0 ]; then
        echo "Error: Division by zero is not allowed."
        return 1
    fi

# Integer remainder (modulus)
    local remainder=$(( num1 % num2 ))

# Floating-point quotient (up to 2 decimal places)
    local quotient=$(echo "scale=2; $num1 / $num2" | bc)

    echo "Quotient: $quotient"
    echo "Remainder: $remainder"
} 

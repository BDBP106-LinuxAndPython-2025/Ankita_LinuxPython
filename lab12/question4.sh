#!/bin/bash
# create the data file
#redirect the numbers to nums.txt
echo "2 3 5 7" > nums.txt

# Read numbers from file into an array
read -ra numbers < nums.txt

# Print the elements of the array
echo "Numbers in the array: ${numbers[@]}"

# Double each number and print
echo "Doubled values are:"
for num in "${numbers[@]}"
do
  echo "$((num * 2))"
done


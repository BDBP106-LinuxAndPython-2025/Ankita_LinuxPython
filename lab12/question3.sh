#!/bin/bash

# Ask for an input number 
echo -n "Enter a number: "
read num

#start a loop for printing the multiplication table of the number upto 15
i=1
until [ $i -gt 15 ]
do
  echo "$num x $i = $((num * i))"
  i=$((i+1))
done


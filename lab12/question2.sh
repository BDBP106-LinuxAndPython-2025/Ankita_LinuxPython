#!/bin/bash

# To print the even numbers between 0 and 50


for (( a=0; a<=50; a++ ))
do
  if (( a % 2 == 0 ))
  then
    echo $a
  fi
done

#another_method
n=0
while [ $n -le 50 ];
do
n=$[$n+1]
done

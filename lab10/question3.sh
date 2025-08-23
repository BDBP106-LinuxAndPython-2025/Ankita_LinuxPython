#!/bin/bash

#A script to check whether file exits 

filename="Heart.csv"
if [ -f "$filename" ];then
	echo "The file exists"
else 
	echo "The file doesn't exist"
fi

#To check if the file is executable

if [ -x "$filename" ]
    then
        echo "The file '$filename' is executable."
else
        echo "The file '$filename' is NOT executable."
fi
~

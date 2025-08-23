#!/bin/bash

#Qs 4 part i:
#A script to check whether file exits 

filename="question2.sh"
if [ -f "$filename" ]; then
    echo "The file exists."
    echo $?
    exit 200
else
    echo "The file does not exist."
    echo $?
    exit 201
fi

#If the echo $? is put before the exit command in the if statement then, it is recognised and hence it will retain the default value of a successfull command which is 0 

#Qs 4 part ii:
if [ -f "$filename" ]; then
    echo "The file exists."
    exit 200
    echo $?
else
    echo "The file does not exist."
    exit 201
     echo $?

fi



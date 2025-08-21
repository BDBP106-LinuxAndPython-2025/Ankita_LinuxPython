#!/bin/bash

#1. Print the HOME variable
echo "HOME directory is: $HOME"

#2. Calculate 23934/44343 using bc and EPF method
result=$(bc << EOF
scale=3
23934/44343
EOF
)
echo "The result is: $result"

#3 List the files in your HOME that start with 'D'
echo "The files with D are: $HOME"
ls "$HOME"/D*


#4 Filter the line(s) in /etc/passwd that have your username 
echo "Lines in /etc/passwd for user $ankitabose:"
grep "$ankitabose:" /etc/passwd 



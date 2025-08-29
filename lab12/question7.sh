#!/bin/bash

# Function to check and manage a directory
function directory_exist {
    local dir_name="$1" 
    if [ -d "$dir_name" ]; then #the d signifies directory
        # Directory exists, list files
        files=$(ls "$dir_name")
        echo "Directory exists. Files: $files"
    else
        # Directory does not exist, create it
        mkdir -p "$dir_name" #we give p since
        echo "Directory created: $dir_path"
    fi
}

# Main script
dir_name=$1 #the user inputs the directory name in the command line
result=$(directory_exist "$dir_name")
echo "$result"

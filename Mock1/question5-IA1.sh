#!/bin/bash

#Reads 4 arguments from the command line

if [ $# -ne 4 ]; then
  echo "Error: Exactly 4 arguments required!"
  exit 1
fi

echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Argument 3: $3"
echo "Argument 4: $4"


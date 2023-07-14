#!/bin/bash

read -p "Enter a file name or directory: " FILE_NAME

if [ -d $FILE_NAME ]
then 
    echo "File is a directory"
    ls -l $FILE_NAME
elif [ -f $FILE_NAME ]
then 
    echo "File is a regular file"
elif [ -x $FILE_NAME ]
then 
    echo "File is an executable"
fi


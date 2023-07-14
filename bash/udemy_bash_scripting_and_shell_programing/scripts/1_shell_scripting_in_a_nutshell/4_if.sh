#!/bin/bash

if [ -e "/etc/shadow" ]
then
    echo "Shadow passwords are enabled."
else
    echo "Dir doesn't exist"
fi
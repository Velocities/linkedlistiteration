#!/bin/bash
FILE=results.txt
if test -f "$FILE"; then
    rm $FILE
fi
./main.py
./second.py

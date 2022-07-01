#!/bin/bash

lines=`cat multi_solutions.txt`

for l in $lines
do
    echo $l
    python split-multiple.py $l
done
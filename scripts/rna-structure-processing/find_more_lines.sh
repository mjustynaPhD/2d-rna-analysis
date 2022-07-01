#!/bin/bash

P="/data/2d-rna/predictions-raw/rna-structure"

for f in $P/*.dot
do
    lines=`cat $f | grep ENERGY | wc -l`
    # echo $lines
    if [ $lines -gt '1' ]
    then
        echo $f
    fi
done
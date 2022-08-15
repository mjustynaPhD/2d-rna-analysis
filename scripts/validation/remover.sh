#!/bin/bash
FILE="to_remove.txt"
FILES=`cat $FILE`
P="predcitions-bpseqs/"

for f in $FILES
do
    m=${f^^}
    echo $P$m
    sudo rm -rf $P$m
done
#!/bin/bash

P="./*"
for id in $P;
do
    if [[ -d $id ]]
    then
        for method in $id/*;
        do
            sudo cp $method/0/whole.bpseq $method/whole.bpseq
            sudo rm -rf $method/0/
        done
    fi
done
#!/bin/bash

DATA="/data/2d-rna/predictions-bpseqs"

for f in $DATA/*;
do
    if [[ "$f" == *-PREDS ]]
    then
        echo $f
        dst=${f/-PREDS/}
        cp -r $f/* $dst
        rm -rf $f
    fi
    if [[ "$f" == *.SEQ ]]
    then
        echo $f
        dst=${f/.SEQ/}
        cp -r $f/* $dst
        rm -rf $f 
    fi


done

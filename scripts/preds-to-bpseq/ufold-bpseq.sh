#!/bin/bash

SRC="/data/2d-rna/predictions-raw/ufold"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.ct;
do
    
    out=${f/$SRC\/}
    out=${out/.ct/}
    # out=${out^^}
    echo $out
    p=/data/2d-rna/predictions-bpseqs/$out/ufold
    echo $p
    # echo $f
    # if [[ ! -d $p ]]
    # then
    sudo docker-compose run --name ufold --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    # fi
done
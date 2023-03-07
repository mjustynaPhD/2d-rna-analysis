#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-raw/spot-rna2"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.bpseq;
do
    
    out=${f/$SRC\/}
    out=${out/.bpseq/}
    # out=${out^^}
    echo $out
    p=/data/2d-rna/new-cifs/predictions-bpseqs/$out/spot-rna2
    echo $p
    # echo $f
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name spot-rna --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    fi
done
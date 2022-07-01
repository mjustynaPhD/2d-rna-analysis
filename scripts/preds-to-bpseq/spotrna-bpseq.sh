#!/bin/bash

SRC="/data/2d-rna/predictions-raw/spot-rna"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.bpseq;
do
    
    out=${f/$SRC\/}
    out=${out/.bpseq/}
    # out=${out^^}
    echo $out
    p=/data/2d-rna/predictions-bpseqs/$out/spot-rna
    echo $p
    # echo $f
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name spot-rna --rm --entrypoint ./rnapdbee rnapdbee -i $f -o /data/2d-rna/predictions-bpseqs/$out/spot-rna
    fi
done
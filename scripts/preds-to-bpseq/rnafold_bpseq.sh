#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-raw/rnafold"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.dot;
do
    
    out=${f/$SRC\/}
    out=${out/.dot/}
    # out=${out^^}
    echo $out
    # echo $f
    p=/data/2d-rna/new-cifs/predictions-bpseqs/$out/rnafold
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name rnafold --rm --entrypoint ./rnapdbee rnapdbee -i $f -o /data/2d-rna/new-cifs/predictions-bpseqs/$out/rnafold
    fi
done
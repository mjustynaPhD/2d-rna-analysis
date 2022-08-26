#!/bin/bash

SRC="/data/2d-rna/new-cifs/ipknot"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.bpseq;
do
    
    out=${f/$SRC\/}
    out=${out/.bpseq/}
    # out=${out^^}
    echo $out
    # echo $f
    p=/data/2d-rna/new-cifs/predictions-bpseqs/$out/ipknot
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name bee-ipknot --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    fi
done
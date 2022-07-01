#!/bin/bash

SRC="/data/2d-rna/predictions-raw/mxfold"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.dbn;
do
    
    out=${f/$SRC\/}
    out=${out/.dbn/}
    # out=${out^^}
    echo $out
    # echo $f
    p=/data/2d-rna/predictions-bpseqs/$out/mxfold
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name mxfold --rm --entrypoint ./rnapdbee rnapdbee -i $f -o /data/2d-rna/predictions-bpseqs/$out/mxfold
    fi
done
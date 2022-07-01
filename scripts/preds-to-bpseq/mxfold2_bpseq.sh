#!/bin/bash

SRC="/data/2d-rna/predictions-raw/mxfold2"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.dbn;
do
    
    out=${f/$SRC\/}
    out=${out/.dbn/}
    # out=${out^^}
    echo $out
    # echo $f
    p=/data/2d-rna/predictions-bpseqs/$out/mxfold2
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name mxfold2 --rm --entrypoint ./rnapdbee rnapdbee -i $f -o /data/2d-rna/predictions-bpseqs/$out/mxfold2
    fi
done
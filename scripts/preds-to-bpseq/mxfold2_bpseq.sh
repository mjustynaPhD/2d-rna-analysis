#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-raw/mxfold2"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.out;
do
    
    out=${f/$SRC\/}
    out=${out/.out/}
    # out=${out^^}
    echo $out
    # echo $f
    p=/data/2d-rna/new-cifs/predictions-bpseqs/$out/mxfold2
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name mxfold2 --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    fi
done
#!/bin/bash

SRC="/data/2d-rna/tmp/rscape-rfam-format"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.dot;
do
    
    out=${f/$SRC\/}
    out=${out/_rfam.dot/}
    # out=${out^^}
    
    # echo $f
    p=/data/2d-rna/tmp/preds_pdbee/$out/rscape
    echo $out $f $p
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name rscape --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    fi
done
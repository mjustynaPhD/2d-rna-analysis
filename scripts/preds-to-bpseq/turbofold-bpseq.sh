#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-raw/turbofold"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.ct;
do
    
    out=${f/$SRC\/}
    out=${out/.ct/}
    # out=${out^^}
    echo $out
    p=/data/2d-rna/tmp/preds_pdbee/$out/turbofold
    echo $p
    # echo $f
    # if [[ ! -d $p ]]
    # then
        sudo docker-compose run --name turbo --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    # fi
done
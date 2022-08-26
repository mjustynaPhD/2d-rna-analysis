#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-raw/e2efold"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.ct;
do
    
    out=${f/$SRC\/}
    out=${out/.seq.ct/}
    # out=${out^^}
    echo $out
    # echo $f
    p=/data/2d-rna/new-cifs/predictions-bpseqs/$out/e2efold
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name e2efold --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    fi
done
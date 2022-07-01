#!/bin/bash

SRC="/data/2d-rna/predictions-raw/rna-structure"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.dot;
do
    
    out=${f/$SRC\/}
    out=${out/.dot/}
    # out=${out^^}
    echo $out
    # echo $f
    p=/data/2d-rna/predictions-bpseqs/$out/rna-structure
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name rnastruct --rm --entrypoint ./rnapdbee rnapdbee -i $f -o /data/2d-rna/predictions-bpseqs/$out/rna-structure
    fi
done
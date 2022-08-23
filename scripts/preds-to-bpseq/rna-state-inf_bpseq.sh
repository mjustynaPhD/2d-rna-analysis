#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-raw/rna-state-inf"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.dot;
do
    
    out=${f/$SRC\/}
    out=${out/-preds.dot/}
    # out=${out^^}

    echo $out
    # echo $f
    p=/data/2d-rna/new-cifs/predictions-bpseqs/$out/rna-state-inf
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name rna-state --rm --entrypoint ./rnapdbee rnapdbee -i $f -o /data/2d-rna/new-cifs/predictions-bpseqs/$out/rna-state-inf
    fi
done
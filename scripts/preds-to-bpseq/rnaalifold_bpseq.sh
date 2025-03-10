#!/bin/bash

SRC="/data/2d-rna/tmp/fasta_alifold"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.dot;
do
    
    out=${f/$SRC\/}
    out=${out/.dot/}
    # out=${out^^}
    echo $out
    # echo $f
    p=/data/2d-rna/tmp/preds_pdbee/$out/rnaalifold
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name rnafold --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    fi
done
#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-raw/contextfold/"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.pred;
do
    out=${f/$SRC\/}
    out=${out/.fa.pred/}
    # out=${out^^}
    # echo $out
    # echo $f
    p=/data/2d-rna/new-cifs/predictions-bpseqs/$out/contextFold
    echo $p

    # if [[ ! -d $p ]]
    # then
    #     echo "Create directory $p"
    #     mkdir -p $p
    # fi
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --rm --entrypoint ./rnapdbee rnapdbee -i $f -o $p
    fi
    
    # docker run rnapdbee:latest ./rnapdbee rnapdbee -i $f -o /data/2d-rna/predictions-bpseqs/$out/contextFold
done
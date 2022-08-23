#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-rna-structure"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*;
do
    # echo $f 
    out=${f/$SRC\/}
    # echo $out
    for dot in $f/*.dot
    do
        # echo $dot
        type=${dot/$f}
        type=${type/.dot/}
        
        echo $out$type
        # p=/data/2d-rna/predictions-bpseqs/$out/rna-structure
        # if [[ ! -d $p ]]
        # then
        sudo docker-compose run --name rnastr2 --rm --entrypoint ./rnapdbee rnapdbee -i $dot -o /data/2d-rna/new-cifs/rna-structure-bpseqs/$out$type
        # fi

    
    done


    # p=/data/2d-rna/predictions-bpseqs/$out/rna-structure
    # if [[ ! -d $p ]]
    # then
    #     sudo docker-compose run --name rnastruct --rm --entrypoint ./rnapdbee rnapdbee -i $f -o /data/2d-rna/rna-structure-bpseqs/$out/$type/rna-structure
    # fi
done
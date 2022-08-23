#!/bin/bash

SRC="/data/2d-rna/new-cifs/predictions-raw/contrafold"
cd ~/2d-analysis/
echo `pwd`
for f in $SRC/*.dbn;
do
    
    out=${f/$SRC\/}
    out=${out/.dbn/}
    # out=${out^^}
    p=/data/2d-rna/new-cifs/predictions-bpseqs/$out/contrafold
    echo $p
    # echo $f
    if [[ ! -d $p ]]
    then
        sudo docker-compose run --name contrafold --rm --entrypoint ./rnapdbee rnapdbee -i $f -o /data/2d-rna/new-cifs/predictions-bpseqs/$out/contrafold
    fi
done
#!/bin/bash

cd /home/macieka/2d-analysis
DATA="/data/2d-rna/u-cifs"
OUT="/data/2d-rna/rnapdbee-cifs"
mkdir $OUT

for f in $DATA/*
do
    out_name=${f/-preprocessed.cif}
    out_name=${out_name/$DATA/$OUT}
    # echo $out_name
    if [ ! -d $out_name ]
    then
        sudo docker-compose run --rm --entrypoint ./rnapdbee rnapdbee -a DSSR -d VARNA -n ONLY_VISUALIZE -i $f -o $out_name
        sudo rm -rf /data/2d-rna/tmp/*
    fi
    # sudo docker-compose run --rm --entrypoint ./rnapdbee rnapdbee -a DSSR -d VARNA -n ONLY_VISUALIZE -i $f -o $out_name
    # sudo rm -rf /data/2d-rna/tmp/*
done

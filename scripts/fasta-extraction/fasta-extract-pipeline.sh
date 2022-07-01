#!/bin/bash

cd /data/2d-rna/
DATA="/data/2d-rna/dbn-cifs"
OUT="/data/2d-rna/fasta-cifs"
mkdir $OUT

for f in $DATA/*
do
    out_name=${f/$DATA/$OUT}
    out_name=${out_name/.dbn/.fa}
    # echo $out_name
    /usr/bin/head -n2 $f > $out_name

done
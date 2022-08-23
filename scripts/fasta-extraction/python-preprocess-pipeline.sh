#!/bin/bash


source ~/.bashrc
source /home/macieka/miniconda3/etc/profile.d/conda.sh

DATA="cifs-awk"
OUT="u-cifs"
cd /data/2d-rna/

mkdir $OUT

conda activate pdbx

for f in $DATA/*
do
    out_name=${f/u.cif/-preprocessed.cif}
    out_name=${out_name/$DATA/$OUT}
    # echo $out_name
    cat $f | scripts/preprocess-cif.py > $out_name
done
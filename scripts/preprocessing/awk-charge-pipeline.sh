#!/bin/bash

cd /data/2d-rna/
DATA="cifs"
OUT="cifs-awk"
mkdir $OUT

for f in $DATA/*
do
    out_name=${f/.cif/u.cif}
    out_name=${out_name/$DATA/$OUT}
    # echo $out_name
    awk -f scripts/pre-preproc.awk < $f > $out_name
done
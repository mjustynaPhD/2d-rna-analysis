#!/bin/bash

CIF="/data/2d-rna/new-cifs/cifs"
FASTA="/data/2d-rna/new-cifs/fasta500"
CSV="/data/2d-rna/new-cifs/rnapdbee-cifs"
OUTPUT="/data/2d-rna/new-cifs/validation-noncanon/"

for f in $FASTA/*.fa
do
    # echo $f
    base=${f/$FASTA}
    base=${base/.fa}
    echo $base
    p=$OUTPUT/$base/Target
    mkdir -p  $OUTPUT/$base/Target
    python make_bpseq_from_csv.py $CSV/$base/0/noncanonical.csv $f $CIF/$base.cif $OUTPUT/$base/Target
done
# 5IT9_1_I
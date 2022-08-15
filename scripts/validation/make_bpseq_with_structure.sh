#!/bin/bash

CIF="/data/2d-rna/cifs"
FASTA="/data/2d-rna/fasta-cifs"
CSV="/data/2d-rna/rnapdbee-cifs"
OUTPUT="/data/2d-rna/validation-noncanon-non0/"

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
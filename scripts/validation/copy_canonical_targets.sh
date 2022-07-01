#!/bin/bash

CIF="/data/2d-rna/cifs"
FASTA="/data/2d-rna/fasta-cifs"
CSV="/data/2d-rna/rnapdbee-cifs"
OUTPUT="/data/2d-rna/validation-canon/"

for f in $FASTA/*.fa
do
    # echo $f
    base=${f/$FASTA}
    base=${base/.fa}
    echo $base
    mkdir -p  $OUTPUT/$base/Target
    cp $CSV/$base/0/whole.bpseq $OUTPUT/$base/Target

done

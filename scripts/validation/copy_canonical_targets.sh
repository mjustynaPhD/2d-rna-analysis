#!/bin/bash

FASTA="/data/2d-rna/new-cifs/fasta500"
CSV="/data/2d-rna/new-cifs/rnapdbee-cifs"
OUTPUT="/data/2d-rna/new-cifs/validation-all/"

for f in $FASTA/*.fa
do
    # echo $f
    base=${f/$FASTA}
    base=${base/.fa}
    echo $base
    mkdir -p  $OUTPUT/$base/Target
    cp $CSV/$base/0/whole.bpseq $OUTPUT/$base/Target

done

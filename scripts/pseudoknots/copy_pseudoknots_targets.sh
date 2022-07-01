#!/bin/bash

FASTA="/data/2d-rna/pseudoknots-bpseqs"
CSV="/data/2d-rna/rnapdbee-cifs"
OUTPUT="/data/2d-rna/validation-pseudoknots/"

for f in $FASTA/*-new.bpseq
do
    # echo $f
    base=${f/$FASTA}
    base=${base/-new.bpseq}
    echo $base
    mkdir -p  $OUTPUT/$base/Target
    cp $f $OUTPUT/$base/Target/
    
done
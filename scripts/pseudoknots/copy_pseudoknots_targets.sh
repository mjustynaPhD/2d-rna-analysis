#!/bin/bash

FASTA="/data/2d-rna/new-cifs/pseudoknots-bpseqs"
CSV="/data/2d-rna/new-cifs/rnapdbee-cifs"
OUTPUT="/data/2d-rna/new-cifs/validation-pseudoknots/"

for f in $FASTA/*-new.bpseq
do
    # echo $f
    base=${f/$FASTA}
    base=${base/-new.bpseq}
    echo $base
    mkdir -p  $OUTPUT/$base/Target
    cp $f $OUTPUT/$base/Target/
    
done
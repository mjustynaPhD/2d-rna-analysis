#!/bin/bash

SOURCE="/data/2d-rna/tmp/fasta_gt/"
OUTPUT="/data/2d-rna/new-cifs/validation-stack/"

for f in $SOURCE/*
do
    echo $f
    base=${f/$SOURCE}
    base=${base/.bpseq}
    echo $base
    mkdir -p  $OUTPUT/$base/Target
    cp $f $OUTPUT/$base/Target/whole.bpseq

done

#!/bin/bash

PATH="/data/2d-rna/tmp/gt_pdbee/"
CSV="/data/2d-rna/new-cifs/rnapdbee-cifs"
OUTPUT="/data/2d-rna/validation-msa/"

for f in $PATH/*
do
    echo $f
    base=${f/$PATH}
    /bin/mkdir -p  $OUTPUT/$base/Target
    /bin/cp $f/0/whole.bpseq $OUTPUT/$base/Target
done

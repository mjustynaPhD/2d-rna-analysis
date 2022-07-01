#!/bin/bash
INPUT="/data/2d-rna/validation-all/"
OUTPUT="/data/2d-rna/rna-struct-validation/all/"
NAMES=`cat rna-struct-validate-ids.txt`

for f in $NAMES
do
    echo $f
    mkdir -p  $OUTPUT/$f/Target
    cp $INPUT/$f/Target/*.bpseq $OUTPUT/$f/Target/
    # cp $CSV/$base/0/whole.bpseq $OUTPUT/$base/Target

done
